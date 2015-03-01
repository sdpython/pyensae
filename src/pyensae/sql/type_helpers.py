"""
@file
@brief  helpers about python types
"""

import decimal
import math


def guess_type_value(x, none=None):
    """
    guess the type of a value
    @param      x           type
    @param      none        if True and all values are empty, return None
    @return                 type

    @warning if an integer starts with a zero, then it is a string
    """
    try:
        int(x)
        if x[0] == '0' and len(x) > 1:
            return str
        else:
            return int if len(x) < 9 else str
    except ValueError:
        try:
            x = float(x)
            return float
        except ValueError:
            if none:
                if x is None:
                    return None
                try:
                    if len(x) > 0:
                        return str
                    else:
                        return None
                except:
                    return None
            else:
                return str


def guess_type_value_type(none=True):
    """
    @param      none        if True and all values are empty, return None
    @return                 the list of types recognized by guess_type_value
    """
    return [None, str, int, float] if none else [str, int, float]


def get_default_value_type(ty, none=True):
    """
    @param      ty          type in guess_type_value_type
    @param      none        if True and all values are empty, return None
    @return                 a default value for this type
    """
    if ty is None and none:
        return None
    elif ty == str:
        return ""
    elif ty == int:
        return 0
    elif ty == decimal.Decimal:
        return decimal.Decimal(0)
    elif ty == float:
        return 0.0
    else:
        raise TypeError("type expected in " + str(guess_type_value_type()))


def guess_type_list(l, tolerance=0.01, none=True):
    """
    guess the type of a list
    @param      l           list
    @param      tolerance   let's denote m as the frequency of the most representative type,
                            and m2 the second one, if m2 > m * tolerance --> str
    @param      none        if True and all values are empty, return None
    @return                 type, length (order of preference (int, float, str))
                            the parameter length has a meaning only for str result
    """
    defa = None if none else str
    length = 0

    if l in [str, float, int, None, decimal.Decimal]:
        raise Exception("this case is unexpected %s" % str(l))

    if len(l) == 0:
        res = defa

    elif len(l) == 1:
        res = guess_type_value(l[0], none)
        if res == str:
            length = len(l[0])

    else:
        count = {}
        for x in l:
            t = guess_type_value(x, none)
            length = max(length, len(x))
            if t in count:
                count[t] += 1
            else:
                count[t] = 1

        val = [(v, k) for k, v in count.items()]
        val.sort(reverse=True)
        if len(val) == 1:
            res = val[0][1]
        elif val[0][0] * tolerance < val[1][0]:
            res = str
        else:
            res = val[0][1]

    if res != str:
        olength = 0
    else:
        if length > 0:
            x = math.log(length) / math.log(2) + 0.99999
            x = int(x)
            olength = math.exp(x * math.log(2)) + 0.9999
            olength = int(olength) * 2
        else:
            olength = length

    return res, olength
