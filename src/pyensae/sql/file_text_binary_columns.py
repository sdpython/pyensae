# coding: latin-1
"""
@file

@brief contains a class which iterations on rows of a text file structured as a table.

"""


import re
import os
import decimal

from pyquickhelper.loghelper import noLOG
from pyquickhelper.loghelper.flog import GetPath
from .file_text_binary import TextFile


class TextFileColumns (TextFile):

    """
    This class opens a text file as if it were a binary file. It can deal with null characters.
    The file is interpreted as a TSV file or file containing columns.
    The separator is found automatically.
    The columns are assumed to be in the first line but it is not mandatory.

    We walk along a file through an iterator, every line is automatically converted into a dictionary ``{ column : value }``.
    If the class was able to guess what type is which column, the conversion will automatically take place.

    @code
    f = TextFileColumns (filename)
            # filename is a file
            # the separator is unknown --> the class automatically determines it
            # as well as the columns and their type
    f.open ()
    for d in f :
        print d        # d is a dictionary
    f.close ()
    @endcode

    @var _force_header      there is a header even if not detected
    @var _force_noheader    there is no header even if detected
    @var _changes           replace the columns name
    @var _regexfix          impose a regular expression to interpret a line instead of the automatically built one
    @var _filter_dict       it is a function which takes a dictionary and returns a boolean which tells if the line must considered or not
    @var _fields            name of the columns (if there is no header)

    Spaces and non-ascii characters cannot be used to name a column.
    This name must be a named group for a regular expression.
    """

    def __init__(self, filename, errors=None, fLOG=noLOG, force_header=False, changes=None,
                 force_noheader=False, regex=None, filter=None, fields=None,
                 keep_text_when_bad_type=False, break_at=-1, strip_space=True,
                 force_sep=None, nb_line_guess=100, mistake=3, encoding="utf-8",
                 strict_separator=False):
        """
        construction
        @param      filename                    filename
        @param      errors                      see str (errors = ...)
        @param      fLOG                        LOG function, see `fLOG <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/loghelper/flog.html#pyquickhelper.loghelper.flog.fLOG>`_
        @param      force_header                defines the first line as columns header whatever is it relevant or not
        @param      changes                     to change the column name, gives the correspondence, example: { "query":"query___" },
                                                it can be a list if there is no header and you want to name any column
        @param      force_noheader              there is no header at all
        @param      regex                       specify a different regular expression (only if changes is a list)
                                                if it is a dictionary, the class will replace the default by the one associated in regex for this field
        @param      filter                      None if there is no filter, otherwise it is a function which takes a dictionary and returns a boolean
                                                which tells if the line must considered or not
        @param      fields                      when the header is not here, these fields will name the columns
        @param      keep_text_when_bad_type     keep the value when the conversion type does not word
        @param      break_at                    if != -1, stop when this limit is reached
        @param      strip_space                 remove space around columns if True
        @param      force_sep                   if != None, impose a column separator
        @param      nb_line_guess               number of lines used to guess types
        @param      mistake                     not more than mistake conversion in numbers are allowed
        @param      encoding                    encoding
        @param      strict_separator            strict number of columns, it assumes there is no separator in the content of every column
        """
        if changes is None:
            changes = {}

        TextFile.__init__(self, filename, errors, fLOG=fLOG, encoding=encoding)

        self._force_header = force_header
        self._force_noheader = force_noheader
        self._changes = changes
        self._regexfix = regex
        self._filter_dict = filter
        self._fields = fields
        self._keep_text_when_bad_type = keep_text_when_bad_type
        self._break_at = break_at
        self._strip_space = strip_space
        self._force_sep = force_sep
        self._nb_guess_line = nb_line_guess
        self._mistake = mistake
        self._strict_separator = strict_separator
        self._encoding = encoding

        if isinstance(changes, list):
            hhhh, _ = 0, len(changes)
            while _ > 0:
                hhhh, _ = hhhh, _ / 10
            forma_ = "c%0" + str(hhhh) + "d"

            self._changes = {}
            for i, c in enumerate(changes):
                self._changes[forma_ % i] = c

            if self._regexfix is not None and \
                    not isinstance(self._regexfix, dict) and \
                    "(?P<" not in self._regexfix:
                reg = re.compile("[(](.+?)[)]")
                fi = reg.findall(self._regexfix)
                if len(fi) != len(changes):
                    raise Exception(
                        "not the same number of fields in regular expression (%d,%d):\n%s\n%s" %
                        (len(fi), len(changes), str(fi), str(changes)))
                exp = []
                for a, b in zip(fi, changes):
                    s = "(?P<%s>%s)" % (b, a)
                    exp.append(s)
                p = self._regexfix.find(")") + 1
                s = self._regexfix[p]
                self._regexfix = s.join(exp)
                self.LOG("split: ", fi)
                self.LOG("new regex: ", self._regexfix)
            else:
                self.LOG("    TextFileColumns (1): regex: ", self._regexfix)
        else:
            self.LOG("    TextFileColumns (2): regex: ", self._regexfix)

    def __str__(self):
        """return the header
        """
        return str(self.__dict__)

    def get_columns(self):
        """
        @return         the columns
        """
        if "_columns" not in self.__dict__:
            raise Exception("there is no available columns")
        return self._columns

    def open(self):
        """
        open the file and find out if there is a header, what are the columns, what are their type...
        any information about which format was found is logged
        """
        if "_header" not in self.__dict__:
            header, columns, sep, regex = self.guess_columns(force_header=self._force_header,
                                                             changes=self._changes,
                                                             force_noheader=self._force_noheader,
                                                             fields=self._fields,
                                                             regex=self._regexfix if isinstance(
                                                                 self._regexfix,
                                                                 dict) else {},
                                                             force_sep=self._force_sep,
                                                             nb=self._nb_guess_line,
                                                             mistake=self._mistake)
            if self._regexfix is not None and not isinstance(
                    self._regexfix, dict):
                regex = self._regexfix
            self._header = header
            self._columns = columns
            self._sep = sep
            try:
                self._regex = re.compile(regex)
            except Exception as e:
                raise Exception(
                    "algorithm problem: (type %s, %s)\nunable to understand a regular expression (file %s)\nexp: %s" %
                    (str(
                        type(e)),
                        str(e),
                        self.filename,
                        regex))
            self._name = {}
            self._nb = 0
            self._conv = {}
            for k, v in self._columns.items():
                self._name[v[0]] = (k, v[1])
                if v[1] in [int, float, decimal.Decimal]:
                    self._conv[v[0]] = v[1]
        self._nb += 1
        TextFile.open(self)

    def close(self):
        """
        close the file and remove all information related to the format,
        next time it is opened, the format will be checked again
        """
        TextFile.close(self)
        self._nb -= 1
        if self._nb == 0:
            del self.__dict__["_header"]
            del self.__dict__["_columns"]
            del self.__dict__["_regex"]
            del self.__dict__["_name"]
            del self.__dict__["_conv"]

    def __iter__(self):
        """iterator
        @return         a dictionary { column_name: value }
        """
        class tempo__:

            def __init__(self, r):
                self.res = r

            def groupdict(self):
                return self.res

        if "_header" not in self.__dict__:
            raise Exception("file not open %s" % self.filename)

        regex_simple = re.compile(self._regex.pattern.replace(">.*)", ">.*?)"))

        nb = 0
        nberr = 0
        nbert = 0
        for line in TextFile.__iter__(self):
            if nb == 0 and self._header:
                nb += 1
                continue

            tempc = line.split(self._sep)

            if len(tempc) == len(self._columns):
                res = {}
                for i, a in enumerate(tempc):
                    res[self._columns[i][0]] = a
                r = tempo__(res)
            elif not self._strict_separator:
                if len(tempc) < len(self._columns):
                    # impossible
                    r = None
                else:
                    # conflicts...
                    r = regex_simple.match(line)
                    if r is None:
                        r = self._regex.match(line)
            else:
                r = None

            if r is None:
                if nberr == 0:
                    self.LOG(self._regex.pattern)
                self.LOG(
                    "error regex",
                    nberr,
                    "unable to interpret line ",
                    nb,
                    ": ",
                    repr(line))
                nberr += 1
                if nberr * 10 > nb and nberr > 4:
                    message = "pattern: %s\n line: %s" % (
                        regex_simple.pattern, line)
                    raise Exception(
                        "(a) there are probably too many errors %d (%d)\n%s" %
                        (nberr, nb, message))
            else:
                res = r.groupdict()
                if self._strip_space:
                    for k in res:
                        res[k] = res[k].strip()
                giveup = False

                for k in res:
                    if k in self._conv:
                        try:
                            if len(res[k]) == 0 and (self._conv[k] == int or self._conv[
                                    k] == float or self._conv[k] == decimal.Decimal):
                                ttt = self._conv[k](0)
                            else:
                                ttt = self._conv[k](res[k])
                            res[k] = ttt
                        except ValueError:
                            nbert += 1
                            if self._keep_text_when_bad_type:
                                if nbert % 1000 == 1:
                                    self.LOG(
                                        "error type",
                                        nbert,
                                        "unable to interpret line (but keep it) ",
                                        nb,
                                        "value",
                                        repr(
                                            res[k]),
                                        " type ",
                                        repr(
                                            self._conv[k]),
                                        " line ",
                                        repr(line))
                            else:
                                self.LOG(
                                    "error type", nbert, "unable to interpret line ", nb, "value", repr(
                                        res[k]), " type ", repr(
                                        self._conv[k]), " line ", repr(line))
                                if nbert * 10 > nb and nbert > 4:
                                    message = "pattern: %s\n line: %s" % (
                                        regex_simple.pattern, line)
                                    raise Exception(
                                        "(b) there are probably too many errors %d\n%s" %
                                        (nberr, message))
                                giveup = True
                                break
                if giveup:
                    continue
                if self._filter_dict is None or self._filter_dict(res):
                    yield res

            nb += 1
            if self._break_at != -1 and nb > self._break_at:
                break

    @staticmethod
    def _store(output, l, encoding="utf-8"):
        """
        store a list of dictionaries into a file (add a header)

        @param      output      filename
        @param      l           list of dictionary key:value
        @param      encoding    encoding
        @warning                format is utf-8
        """
        sepline = "\n"  # GetSepLine ()
        f = open(output, "w", encoding=encoding)
        nbline = 0
        for d in l:
            if nbline == 0:
                keys = list(d.keys())
                keys.sort()
                f.write("\t".join(keys) + sepline)

            val = [str(d[k]) for k in keys]
            s = "\t".join(val)
            f.write(s + sepline)

            nbline += 1
        f.close()

    def sort(self, output, key, maxmemory=2 ** 28, folder=None, fLOG=noLOG):
        """sort a text file, even a big one, one or several columns gives the order
        @param      output      output file result
        @param      key         lines sorted depending of these columns
        @param      maxmemory   a file is split into smaller files which contains not more than maxmemory lines
        @param      folder      the function needs to create temporary files, this folder will contain them
                                before they get removed
        @param      fLOG        logging function
        @return

        @warning  We assume this file is not opened.
        """
        if isinstance(key, str):
            key = (key,)
        if folder is None:
            folder = GetPath()
        if not os.path.exists(folder):
            raise Exception("unable to find folder %s" % folder)

        try:
            file = open(output, "w", encoding=self._encoding)
            file.close()
        except Exception as e:
            raise Exception(
                "unable to create file %s, reason: %s" %
                (output, str(e)))

        self.LOG("sorting file ", self.filename)
        #root   = self.filename.replace (":", "_").replace ("/", "_").replace ("\\", "_").replace (".", "_")
        files = []
        memo = []
        self.open()
        for line in self:
            try:
                k = tuple([line[k] for k in key])
            except KeyError as e:
                raise Exception("unable to find one column in\n{0}".format(
                    self.get_columns())) from e
            memo.append((k, line))
            if len(memo) > maxmemory:
                memo.sort(key=lambda el: el[0])
                memo = [l[1] for l in memo]
                tempout = os.path.join(folder, "root_%05d.txt" % len(files))
                self.LOG("writing file %d lines in " % len(memo), tempout)
                TextFileColumns._store(tempout, memo)
                files.append(tempout)
                memo = []

        if len(memo) > 0:
            memo.sort(key=lambda el: el[0])
            memo = [l[1] for l in memo]
            tempout = os.path.join(folder, "root_%05d.txt" % len(files))
            self.LOG("writing file %d lines in " % len(memo), tempout)
            TextFileColumns._store(tempout, memo)
            files.append(tempout)
            memo = []

        self.close()

        TextFileColumns.fusion(
            key,
            files,
            output,
            force_header=self._force_header,
            fLOG=self.LOG)
        for m in files:
            self.LOG("removing ", m)
            os.remove(m)

    @staticmethod
    def fusion(key, files, output, force_header=False, encoding="utf-8", fLOG=noLOG):
        """
        does a fusion between several files with the same columns (different order is allowed)
        @param      key             columns to be compared
        @param      files           list of files
        @param      output          output file
        @param      force_header    impose the first line as a header
        @param      encoding        encoding
        @param      fLOG            logging function
        @warning We assume all files are sorted depending on columns in key
        """
        fh = []
        for f in files:
            h = TextFileColumns(f, force_header=force_header,
                                encoding=encoding, fLOG=fLOG)
            h.open()
            fh.append([h, iter(h)])

        res = open(output, "w", encoding=encoding)
        nbline = 0
        sepline = "\n"  # GetSepLine ()
        if isinstance(key, str):
            key = [key]

        # start
        kline = []
        for li in fh:
            try:
                if li[1] is None:
                    d = None
                else:
                    d = li[1].__next__()
            except StopIteration:
                d = None
            if d is not None:
                try:
                    k = tuple([d[k] for k in key])
                except KeyError as e:
                    raise Exception("unable to find one column in\n{0}".format(
                        li[0].get_columns())) from e
                kline.append([k, d] + li)

        # loop
        while len(kline) > 0:

            # minimum
            mi = None
            for i, line in enumerate(kline):
                if mi is None or line[0] < mi:
                    mi = line[0]
                    pos = i

            # picking
            line = kline[pos]
            del kline[pos]

            # adding
            d = line[1]
            if nbline == 0:
                keys = list(d.keys())
                keys.sort()
                res.write("\t".join(keys) + sepline)

            val = [str(d[k_]) for k_ in keys]
            s = "\t".join(val)
            res.write(s + sepline)
            nbline += 1

            # next
            try:
                d = line[-1].__next__()
            except StopIteration:
                d = None

            if d is not None:
                k = tuple([d[k_] for k_ in key])
                kline.append([k, d] + line[2:])

        # end
        for li in fh:
            li[0].close()
        res.close()
