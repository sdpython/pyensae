"""
To speed up the unit testing of the module
"""


def get_codes(envvar):
    """
    if a given file is present, connect itself to the cluster
    """
    import os
    val = os.environ.get(envvar, None)
    if val is None:
        return val
    else:
        return val.split("**")


if __name__ == "__main__":
    print(get_codes())
