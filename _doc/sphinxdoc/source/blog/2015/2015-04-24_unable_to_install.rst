

.. blogpost::
    :title: Unable to install the module on OS X
    :keywords: OS X, pip
    :date: 2015-04-24
    :categories: installation
    
    The module is tested on Windows and on Linux 
    through `travis <https://travis-ci.org/sdpython/pyensae>`_.
    It is not tested on OS X (Apple), the installation was failing
    on a student's machine today (however he installed almost 
    all the version including 3.5a). 
    
    In that is the case, I recommend to install *pyensae* and 
    *pyquickhelper* without their dependencies::
    
        pip install <module> --no-deps
        
