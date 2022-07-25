from antlr4 import *


class CSharpLexerBase(Lexer):
    def __init__(self, input, output):
        Lexer.__init__(self, input, output)

        self.interpolatedStringLevel = 0
        self.interpolatedVerbatiums = []
        self.curlyLevels = []
        self.verbatium = False

    def OnInterpolatedRegularStringStart(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(False)
        verbatium = False

    def OnInterpolatedVerbatiumStringStart(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(True)
        self.verbatium = True

    def OnOpenBrace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels.append(curlyLevels.pop() + 1)

    def OnCloseBrace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels.append(curlyLevels.pop() - 1)
            if self.curlyLevels.Peek() == 0:
                self.curlyLevels.pop()
                self.Skip()
                popMode()

    def OnColon(self):
        if self.interpolatedStringLevel > 0:
            ind = 1
            switchToFormatString = True
            while _input.La(ind) != '}':
                if _input.La(ind) == ':' or _input.La(ind) == ')':
                    switchToFormatString = False
                    break
                ind += 1
            if switchToFormatString:
                self.Mode(Test.CSharpLexer.INTERPOLATION_FORMAT)

    def OpenBraceInside(self):
        self.curlyLevels.append(1)

    def OnDoubleQuoteInside(self):
        self.interpolatedStringLevel -= 1
        self.interpolatedVerbatiums.pop()
        self.verbatium = self.interpolatedVerbatiums.Peek(
        ) if self.interpolatedVerbatiums.Count() > 0 else False

    def OnCloseBraceInside(self):
        self.curlyLevels.pop()

    def IsRegularCharInside(self):
        return not self.verbatium

    def IsVerbatiumDoubleQuoteInside(self):
        return self.verbatium
