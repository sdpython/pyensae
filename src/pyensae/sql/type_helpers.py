"""
@file
@brief  helpers about python types
"""

import decimal


def guess_type_value(x, none=None):
    """
    Guesses the type of a value.

    @param      x           type
    @param      none        if True and all values are empty, return None
    @return                 type

    @warning if an integer starts with a zero, then it is a string
    """
    if isinstance(x, int):
        return int
    elif isinstance(x, float):
        try:
            int(x)
            return int if int(x) == x else float
        except Exception:
            return float
    else:
        if none:
            if x is None:
                return None
            try:
                if len(x) > 0:
                    return str
                else:
                    return None
            except Exception:
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
