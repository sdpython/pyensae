# coding: latin-1
"""
@file

@brief contains a class which opens a text file as a binary file.
"""


import re
import os
import math
import time
import decimal

from .type_helpers import guess_type_value


class TextFile:

    """
    This class opens a text file as if it were a binary file. It can deal with null characters which are missed by open function.

    @var    filename        file name
    @var    utf8            decode in utf8?
    @var    errors          decoding in utf8 can raise some errors, see `str <https://docs.python.org/3.4/library/stdtypes.html?highlight=str#str>`_ to understand the meaning of this parameter
    @var    LOG             logging function
    @var    _buffer_size    read a text file _buffer_size bytes each time
    @var    _filter         function filter, None or return True or False whether a line should considered or not

    Example:
    @code
    f = TextFile (filename)
    f.open ()
    for line in f :
        print line
    f.close ()
    @endcode
    """

    _split_expr = re.compile("\\r?\\t", re.U)
    _sep_available = "\t;,| "

    def __init__(self, filename,
                 utf8=True,
                 errors=None,
                 fLOG=print,
                 buffer_size=2 ** 20,
                 filter=None,
                 separated=False):
        """
        construction
        @param      filename        filename
        @param      utf8            True or False
        @param      errors          see str (errors = ...)
        @param      fLOG            LOG function, see `fLOG <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/loghelper/flog.html#pyquickhelper.loghelper.flog.fLOG>`_
        @param      buffer_size     buffer_size (mostly use to test the reading function)
        @param      filter          None if there is no filter, otherwise it is a function which takes a list and returns a boolean
                                    which tells if the line must considered or not
        @param      separated       if True, the line returned by the iterator are splitted by the most probable separator
        """
        self.filename = filename
        self.utf8 = utf8
        self.errors = errors
        self.LOG = fLOG
        self._buffer_size = buffer_size
        self._filter = filter
        self._separated = separated

    def open(self):
        """open the file in reading mode
        """
        self.LOG("  TextFile: opening file ", self.filename)
        if self._separated:
            res = self.guess_columns()
            self.LOG("   TextFile: guessed: ", res)
            sep = res[2]
            self._separated_value = sep

        self._f = open(
            self.filename,
            "r",
            encoding="utf8") if self.utf8 else open(
            self.filename,
            "r")
        self._nbline = 0
        self._read = 0

    def close(self):
        """close the file
        """
        self._f.close()
        self.LOG("  TextFile: closing file ", self.filename)
        del self.__dict__["_f"]

    def get_nb_readlines(self):
        """returns the number of read lines
        """
        return self._nbline

    def get_nb_readbytes(self):
        """returns the number of read bytes
        """
        return self._nbline

    def readlines(self):
        """extracts all the lines,
        the file must not be opened through method open
        \n are removed
        """
        self.open()
        res = []
        for line in self:
            l = line.strip("\r\n")
            res.append(l)
        self.close()
        return res

    def __iter__(self):
        """iterator
        @code
        f.open ()
        for line in f :
            ...
        f.close ()
        @endcode

        @return         a str string
        """
        if "_f" not in self.__dict__:
            raise Exception("file %s is not opened." % self.filename)
        filesize = os.stat(self.filename).st_size
        size = self._buffer_size
        blin = self._f.read(size)
        self._read = len(blin)

        if blin.startswith("\xef\xbb\xbf"):
            self.LOG("  removing the three first character u'\\xef\\xbb\\xbf'")
            blin = blin[3:]
        if blin.startswith("\ufeff"):
            self.LOG("  removing the three first character u'\\ufeff'")
            blin = blin[len("\ufeff"):]

        endline = "\n"
        endchar = "\r"

        begin = 0
        sel = 0
        tim = time.clock()
        while len(blin) > 0:

            pos = blin.find(endline, begin)
            if pos == -1:
                pos = blin.find(endchar, begin)
                if begin == 0 and pos != -1:
                    self.LOG("  problem in file ", self.filename)
                    self.LOG("  the line separator is not \\n but \\r")

            while pos == -1:
                if begin > 0:
                    blin = blin[begin:]
                    begin = 0
                temp = self._f.read(size)
                self._read += len(temp)
                blin += temp
                pos = blin.find("\n")
                if pos == -1:
                    pos = blin.find("\r", begin)
                if len(temp) == 0 and pos == -1:
                    pos = len(blin)

            temp = blin[begin:pos]
            line = str(temp)
            begin = pos + 1

            tim2 = time.clock()
            if tim2 - tim > 60:
                tim = tim2
                ratio = float(self._read) / filesize * 100
                self.LOG(
                    "  processing line ",
                    self._nbline,
                    " read bytes ",
                    self._read,
                    " sel ",
                    sel,
                    " ratio %2.2f" %
                    ratio,
                    "%")

            if self.utf8:
                r = line
                # if self.errors != None :
                #    try :
                #        r = line.encode("utf8")
                #    except UnicodeDecodeError :
                #        self.LOG ("  Unicode error with line ", self._nbline, repr (line))
                #        r = line.encode("utf8", errors = self.errors)
                # else :
                #    try :
                #        r = line.encode("utf8")
                #    except UnicodeDecodeError as e :
                #        try :
                #            r = line.encode("latin-1")
                #        except UnicodeDecodeError as ee :
                #            message = str (e)
                #            temp = ("-----------nbline %d in file %s\n" % (self._nbline,self.filename)) + repr (line) + "\n" + message + "\n"
                #            self.LOG (temp)
                #            raise Exception (temp)
                r = r.rstrip(endchar)
                if self._filter is None or self._filter(r):
                    if self._separated:
                        yield r.split(self._separated_value)
                    else:
                        yield r
            else:
                if self._filter is None or self._filter(line):
                    if self._separated:
                        yield line.split(self._separated_value)
                    else:
                        yield line

            self._nbline += 1

    def _load(self, filename, this_column, file_column, prefix, **param):
        """
        load...
        """
        f = TextFile(filename, fLOG=self.LOG, **param)
        f.open()
        cont = {}
        for line in f:
            if f.get_nb_readlines() == 0:
                columns = self._interpret_columns(line)
            else:
                col = self._interpret(line)
                key = col[columns[file_column]]
                cont[key] = col
        f.close()
        return cont, columns, this_column, file_column, prefix

    def _interpret_columns(self, line):
        """interpret the first line which contains the columns name
        @param      line        string
        @return                 dictionary { name:position }"""
        col = self._interpret(line)
        res = {}
        for i in range(0, len(col)):
            res[col[i]] = i
        return res

    def _interpret(self, line):
        """split a line into a list, separator \\t
        @param      line        string
        @return                 list
        """
        col = TextFile._split_expr.split(line.strip(" \r\n"), fLOG=self.LOG)
        return col

    def join(self, definition,
             output,
             missing_value="",
             unique=None,
             **param):
        """join several files together

        @param  definition      list of triplets:
                                    filename, this_column, file_column, prefix
        @param  output          if None, return the results as a list, otherwise save it into output
        @param  param           parameter used to open files
        @param  missing_value   specify a value for the missing values
        @param  unique          if unique is a column name, do not process a line whose value has already been processed, None otherwise
        @return                 columns, matrix or number of of missing values

        We assume that every file starts with header giving columns names.
        The functions associates this_column value to file_column and append all the columns from filename with a prefix.
        We also assumes values in file_column are unique.
        """
        if output is not None:
            output = open(output, "w", encoding="utf-8")

        files = []
        for a, b, c, d in definition:
            files.append(self._load(a, b, c, d, **param))

        res = []
        miss = 0
        uniquekey = {}

        self.open()
        for line in self:
            if self.get_nb_readlines() == 0:
                columns = self._interpret_columns(line)
                oldnb = len(columns)
                last = max(columns.values()) + 1
                for file in files:
                    col = file[1]
                    pre = file[-1]
                    for k, v in col.items():
                        columns[pre + k] = last + v
                    last += len(col)
                linecol = ["" for c in columns]
                for k, v in columns.items():
                    linecol[v] = k

                if output is None:
                    res.append(linecol)
                else:
                    output.write("\t".join(linecol) + "\n")

                s1 = len(linecol)
                s2 = oldnb
                for f in files:
                    s2 += len(f[1])
                if s1 != s2:
                    mes = "size problem %d != " % (s1)
                    mes += " + ".join([str(x)
                                       for x in [oldnb, ] + [len(f[1]) for f in files]])
                    raise Exception(mes)

            else:
                col = self._interpret(line)

                if unique is not None:
                    key = columns[unique]
                    val = col[key]
                    if val in uniquekey:
                        uniquekey[val] += 1
                        continue
                    else:
                        uniquekey[val] = 1

                if len(col) != oldnb:
                    col.extend(["" for i in range(0, oldnb - len(col))])
                if len(col) != oldnb:
                    mes = "line %d: problem len(col) = %d and oldnb = %d\n%s" % (
                        self.get_nb_readlines(), len(col), oldnb, repr(line))
                    raise Exception(mes)

                for file in files:
                    cont = file[0]
                    c = file[1]
                    this_key = col[columns[file[2]]]
                    if this_key in cont:
                        val = cont[this_key]
                        if len(val) != len(c):
                            mes = "line %d: problem len(val) = %d and len (c) = %d" % (
                                self.get_nb_readlines(), len(val), len(c))
                            raise Exception(mes)
                    else:
                        val = [missing_value for k in c]
                        miss += len(val)
                    col.extend(val)

                if len(col) != len(columns):
                    mes = "problem 1 with line %d\n" % self.get_nb_readlines()
                    mes += "len (col) = %d len (columns) = %d" % (len(col),
                                                                  len(columns))
                    raise Exception(mes)

                if len(("\t".join(col)).split("\t")) != len(col):
                    mes = "problem 2 with line %d\n" % self.get_nb_readlines()
                    mes += "len (col) = %d len (columns) = %d" % (
                        len(("\t".join(col)).split("\t")), len(columns))
                    raise Exception(mes)

                if output is None:
                    res.append(col)
                else:
                    output.write("\t".join(col) + "\n")

        if output is None:
            return res
        else:
            output.close()
            return miss

    def _count_s(self, car):
        """returns the number of every character in car
        """
        res = {}
        for i, c in enumerate(car):
            if c in res:
                res[c] += 1
            else:
                res[c] = 1
        return res

    def _get_type(self, s):
        """guess the type of value s
        """
        return guess_type_value(s)

    def guess_columns(self, nb=100,
                      force_header=False,
                      changes={},
                      force_noheader=False,
                      fields=None,
                      regex={},
                      force_sep=None,
                      mistake=3):
        """guess the columns type
        @param      nb              number of lines to have a look to in order to find all the necessary elements
        @param      force_header    impose a header whether it is detect or not
        @param      changes         modify some column names, example { "query":"query___" }
        @param      force_noheader  there is no header at all
        @param      fields          name of the columns if there is no header (instead of c000, c001...)
        @param      regex           if the default expression for a field is not the expected one, change by looking into regex
        @param      force_sep       force the separator to be the one chosen by the user (None by default)
        @param      mistake         not more than mistake conversion in numbers are allowed
        @return                     4-tuple
                                        - True or False: presence of a header (it means there is at least one numerical column)
                                        - column definition { position : (name, type) } or { position : (name, (str, max_length*2)) }
                                        - separator
                                        - regex which allow the user to extract information from the file

        The column separator is looked into ``, | ; \\t``
        @warning The file must not be opened, it will be several times.
        """
        self.LOG("  TextFile.guess_columns: processing file ", self.filename)

        endlinechar = "\n "

        # n lines
        temp = TextFile(self.filename, fLOG=self.LOG)
        lines = []

        temp.open()
        for line in temp:
            line = line.strip(endlinechar)
            if len(line) == 0:
                continue
            lines.append(line)
            if len(lines) > nb:
                break
        self.LOG("  TextFile.guess_columns: using ", len(lines), " lines")
        temp.close()

        # guess the separation
        sep = TextFile._sep_available
        if force_sep is not None and force_sep not in force_sep:
            sep += force_sep
        h = {}
        mx = 0
        for line in lines:
            co = self._count_s(line)
            for s in sep:
                n = co.get(s, 0)
                if n == 0:
                    continue
                k = s, n
                if k not in h:
                    h[k] = 1
                else:
                    h[k] += 1
                mx = max(n, mx)

        mx += 1
        best = None
        iner = None
        for c in sep:
            m = {}
            z = 0
            for k in range(mx):
                if (c, k) in h:
                    m[k] = h[c, k]
                    z += k * m[k]

            if len(m) == 0:
                continue
            g = max(sum(m.values()), len(lines))
            if z < max(len(lines) * 9 / 10, 1):
                continue

            for k in m:
                m[k] = float(m[k]) / g
            s = 0.0
            for k in m:
                s += m[k] * math.log(m[k])
            if iner is None or s > iner:
                iner = s
                best = c

        bestsep = best

        if force_sep is not None and bestsep != force_sep:
            self.LOG(
                "  TextFile.guess_columns: changes the separator",
                repr(force_sep))
            bestsep = force_sep

        bestcol = 0
        bestnb = 0
        for k in range(mx):
            if (bestsep, k) in h:
                if bestnb < h[bestsep, k]:
                    bestnb = h[bestsep, k]
                    bestcol = k + 1

        self.LOG(
            "  TextFile.guess_columns: sep ",
            repr(bestsep),
            "nb cols",
            bestcol,
            " bestnb ",
            bestnb,
            " more ",
            h)

        # determine the type of every column

        h = {}
        for line in lines:
            cols = line.split(bestsep)
            for i in range(len(cols)):
                ty = self._get_type(cols[i])
                k = i, ty
                if k not in h:
                    h[k] = 1
                else:
                    h[k] += 1

        columns = {}
        for a in h:
            k, t = a
            if k >= bestcol:
                continue
            if k not in columns:
                columns[k] = (t, h[a])
            elif h[a] > columns[k][1]:
                columns[k] = (t, h[a])

        for pos in columns:
            # int and float corrections
            if columns[pos][0] == int and h.get((pos, float), 0) > 0:
                self.LOG(
                    "  changing column type ",
                    pos,
                    columns[pos],
                    " into ",
                    float)
                columns[pos] = (float, h[pos, float] + h[pos, int])
            su = h.get((pos, str), 0)
            if (columns[pos][0] == int or columns[pos][0] == float or columns[
                    pos][0] == decimal.Decimal) and su > mistake:
                self.LOG(
                    "  changing column type ",
                    pos,
                    columns[pos],
                    " into ",
                    str,
                    " mistakes ",
                    su,
                    " > ",
                    mistake)
                columns[pos] = (str, columns[pos][1] + su)

        # header or not

        mat = 0
        no = 0
        cols = lines[0].split(bestsep)
        for i, c in enumerate(cols):
            t = self._get_type(c)
            e = columns.get(i, (str, 0))[0]
            if e != str:
                if t == e:
                    mat += 1
                else:
                    no += 1
        header = not force_noheader and (force_header or (no > mat))

        # determine the column name

        if header:
            names = lines[0].split(bestsep)
            del lines[0]
            if len(names) != bestcol:
                raise Exception(
                    "unable to continue: the header does not contain the same number of columns %s != %s" %
                    (len(names), bestcol))
        elif fields is not None:
            if len(fields) != bestcol:
                raise Exception(
                    "the number of fields (%d) is different of the number of columns found in the file %d" %
                    (len(fields), bestcol))
            names = fields
        else:
            hhhh, _ = 0, bestcol
            while _ > 0:
                hhhh, _ = hhhh, _ / 10
            format = "c%0" + str(hhhh) + "d"
            names = [format % i for i in range(bestcol)]

        for k in columns:
            if k >= len(names):
                raise Exception(
                    "incoherence in the file being read: %d >= %d: " %
                    (k, len(names)) + repr(names) + "\n" + repr(columns))
            columns[k] = (changes.get(names[k], names[k]), columns[k][0])

        self.LOG(
            "  TextFile.guess_columns: header ",
            header,
            " columns ",
            columns)
        coy = columns.copy()

        # end
        exp = self._build_regex(bestsep, columns, regex=regex)
        self.LOG("  TextFile.guess_columns: regex ", exp)

        # determines the length of columns
        length = {}
        no = 0
        for line in lines:
            spl = line.split(bestsep)
            if len(spl) != len(columns):
                continue
            no += 1
            for i, c in enumerate(spl):
                vl = length.get(i, 0)
                if vl < len(c):
                    length[i] = len(c)

        for c in columns:
            v = columns[c]
            if v[1] == str and c in length and length[c] > 0:
                v = (v[0], (v[1], length[c] * 2))
                columns[c] = v

        if coy != columns:
            self.LOG(
                "  TextFile.guess_columns: header ",
                header,
                " columns ",
                columns)

        return header, columns, bestsep, exp

    def count_rejected_lines(self, header, exp, output=None):
        """
        count the number of rejected lines by regular expression exp

        @param      header          header or not in the first line
        @param      exp             regular expression
        @param      output          if != None, output is a stream which will receive the unrecognized line (see below)
        @return                     nb_accepted, nb rejected

        Format for the file containing the unrecognized lines:
        @code
        line number \t  line
        @endcode

        """
        if isinstance(exp, str):
            exp = re.compile(exp, re.U)
        acc, rej = 0., 0.
        temp = TextFile(self.filename, fLOG=self.LOG)
        temp.open()
        nb = 0
        for line in temp:
            nb += 1
            if header and acc + rej == 0:
                header = False
                continue
            if len(line) == 0:
                continue
            r = exp.search(line)
            if r:
                acc += 1
            else:
                rej += 1
                if output is not None:
                    output.write("%d\t%s\n" % (nb - 1, line))
        temp.close()
        return acc, rej

    _build_regex_default_value_types = {int: "([-]?[1-9][0-9]*?)|(0?)",
                                        decimal.Decimal: "([-]?[1-9][0-9]*?L?)|(0?)",
                                        float: "[-]?[0-9]*?([.][0-9]*?)?([eE][-]?[0-9]{0,4})?",
                                        str: ".*"}

    def _build_regex(self,
                     sep,
                     columns,
                     exp=_build_regex_default_value_types,
                     nomore=False,
                     regex={}):
        """
        Build a regular expression.

        @param          sep             separator
        @param          columns         columns definition
        @param          exp             regular expression associated to each type, (see below for the default value)
        @param          nomore          private argument, no more try, not possible to simplify
        @param          regex           if the default expression for a field is not the expected one, look into regex if there is one
        @return                         regex

        Default value for ``exp``:

        @code
            {
                int:             "([-]?[1-9][0-9]*?)|(0?)",
                decimal.Decimal: "([-]?[1-9][0-9]*?L?)|(0?)",
                float:           "[-]?[0-9]*?([.][0-9]*?)?([eE][-]?[0-9]{0,4})?",
                str:             ".*"
            }
        @endcode

        """
        mx = max(columns.keys()) + 1
        res = [None for i in range(mx)]
        for k, v in columns.items():
            t = v[1]
            if t not in exp:
                raise Exception("unknown type %s" % str(t))
            if v[0] in regex:
                res[k] = (v[0], regex[v[0]])
            else:
                res[k] = (v[0], exp[t])
        res = ["(?P<%s>%s)" % c for c in res]
        if sep == "\t":
            sep = "\\t"
        final = "^%s$" % sep.join(res)

        try:
            self.LOG("  compiling", final)
            exp = re.compile(final)
            return final
        except Exception as e:
            if "but this version only supports 100 named groups" in str(e):
                self.LOG(
                    "  problem with expression (more than 100 groups) ",
                    final)
            if nomore:
                if "bad character in group name" in str(e):
                    reg = re.compile("?P<(.*?)>")
                    all = reg.findall(final)
                    s = ",".join(all)
                    raise Exception(
                        "this expression does not compile (%s), pattern %s, columns %s" %
                        (str(e), final, s))
                else:
                    raise Exception(
                        "this expression does not compile (%s), pattern %s" %
                        (str(e), final))

        exp = {int: "[-]?[0-9]*?",
               float: "[0-9.eE]*?",
               str: ".*"}
        return self._build_regex(sep, columns, exp, True)
