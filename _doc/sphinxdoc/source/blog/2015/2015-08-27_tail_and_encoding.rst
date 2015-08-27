

.. blogpost::
    :title: Tail of a text file encoded in utf-8
    :keywords: text file, encoding, utf-8
    :date: 2015-08-27
    :categories: bug, encoding
    
    Funny thing I went through when I wanted to get the tail of 
    a text file::
    
        with open(filename, "r", encoding="utf8") as f:
            rows = f.readlines()
        tail = rows[-10:] if len(rows) > 10 else rows
    
    When the file is too big, it is really tempting to do::
    
        with open(filename, "r", encoding="utf8") as f:
            f.seek(size - threshold)  # added line
            rows = f.readlines()
        tail = rows[-10:] if len(rows) > 10 else rows

    However, because of the encoding, the cursor might fall
    in the middle of an utf8 character (they can have 1 or 2 character).
    In that case, the next instruction ``readlines`` fails
    because of an encoding error.
    The cursor needs to be moved by one character.
    See function :func:`file_tail <pyensae.file_hiler.content_helper.file_tail>`.