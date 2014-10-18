"""
@file
@brief Various functions to process text
"""

def replace_comma_by_point(file) :
    """
    replaces all commas by point in a file (do that inplace)
    
    @param      file        file to process
    """
    with open(file,"r") as f : text = f.read()
    text = text.replace(",",".")
    with open(file,"w") as f : f.write(text)
