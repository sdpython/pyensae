"""
To speed up the unit testing of the module
"""
def get_codes():
    """
    if a given file is present, connect itself to the cluster
    """
    import os, sys
    if sys.platform.startswith("win"):
        f = [ ".." ] * 5
    else:
        f = [ ".." ] * 3
    fold = os.path.abspath(os.path.dirname(__file__))
    f = os.path.normpath(os.path.join(fold, *f))
    files = os.listdir(f)
    fold=f
    for f in files:
        f = os.path.join(fold,f)
        if os.path.isfile(f) and f != "." and "code" in f:
            with open(f,"r") as f:
                lines = f.readlines()
                f = [ _.strip() for _ in lines ]
                return [ _ for _ in f if len(_) > 0 ]
    return None

if __name__ == "__main__":
    print(get_codes())