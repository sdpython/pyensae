"""
@file
@brief Convert R into Python
"""
from antlr4 import ParseTreeWalker
from pyquickhelper.pycode import remove_extra_spaces_and_pep8
from .RParser import RParser
from .RLexer import RLexer
from .antlr_grammar_use import parse_code
from .rconverterListener import TreeStringListener


def r2python(code: str, pep8=False, fLOG=None) -> str:
    """
    Converts a R script into Python.

    :param code: R string
    :param pep8: modify the output to be compliant with pep8
    :param fLOG: logging function
    :return: Python string

    .. _code-r2python:

    The function uses a customized R grammar implemented with Antlr4.
    Formula becomes strings. They should be handled with
    `patsy <http://patsy.readthedocs.io/en/latest/>`_.

    .. exref::
        :title: Convert R into Python

        .. runpython::
            :showcode:

            rscript = '''
                nb=function(y=1930){
                debut=1816
                MatDFemale=matrix(D$Female,nrow=111)
                colnames(MatDFemale)=(debut+0):198
                cly=(y-debut+1):111
                deces=diag(MatDFemale[:,cly[cly%in%1:199]])
                return(c(B$Female[B$Year==y],deces))}
                '''

            from pyensae.languages.rconverter import r2python
            print(r2python(rscript, pep8=True))

    Some patterns are not well migrated such expression ``a:b`` into ``range(a,b)``.
    The grammar could be improved to detect the beginning of the expression but
    for now, if the function fails to do the conversion, ``a:b`` must be written
    into ``(a):b``. The same trick is sometimes needed for other patterns
    such as the operator ``%in%`` which is converted into an intersection
    of two sets.

    Kwonws bugs:

    * ``} else {`` needs to be replaced by ``} EOL else {``
    * comment added at the end of line must be followed by an empty line
    * ``m[,1]`` must be replaced by ``M[:,1]``
    * formula ``~.`` is not translated
    * ``%<%`` cannot be followed by an empty line

    The grammar were updated in 2022 for python 3.10 and
    :epkg:`antlr4-python3-runtime` == 4.10.
    """
    if fLOG:
        fLOG(  # pragma: no cover
            "[r2python] parse ", len(code), "bytes")
    parser = parse_code(code, RParser, RLexer)
    if fLOG:
        fLOG(  # pragma: no cover
            "[r2python] parse continue")
    parsed = parser.parse()
    if fLOG:
        fLOG(  # pragma: no cover
            "[r2python] listen")
    listen = TreeStringListener(parsed, fLOG=fLOG)
    walker = ParseTreeWalker()
    if fLOG:
        fLOG(  # pragma: no cover
            "[r2python] walk")
    walker.walk(listen, parsed)
    if fLOG:
        fLOG(  # pragma: no cover
            "[r2python] get code")
    code = listen.get_python()
    if pep8:
        if fLOG:
            fLOG(  # pragma: no cover
                "[r2python] pep8")
        code = remove_extra_spaces_and_pep8(code, aggressive=True)
    return code
