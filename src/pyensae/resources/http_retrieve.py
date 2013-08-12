"""
@file
@brief Various functions to get data from a website, a reference website.
"""
import os, sys, importlib, re, urllib.request 

def remove_empty_line(file) :
    """
    remove empty line in an imported file
    
    @param      file        local file name
    """
    try :
        f = open(file,"r")
        lines   = f.readlines ()
        f.close ()
        encoding = None
    except UnicodeDecodeError:
        try :
            f = open(file,"r", encoding="latin-1")
            lines   = f.readlines ()
            f.close ()
            encoding = "latin-1"
        except UnicodeDecodeError:
            f = open(file,"r", encoding="utf8")
            lines   = f.readlines ()
            f.close ()
            encoding = "utf8"
        
    nbrn    = len( [ _ for _ in lines if _.endswith("\n") ])
    lines   = [ _.rstrip(" \n") for _ in lines ]
    nbempty = len ( [ _ for _ in lines if len(_) == 0 ] )
    skip    = 0
    if nbempty + nbrn > len(lines) / 3 :
        res   = lines
        lines = []
        last  = -1
        for i,line in enumerate(res) :
            if len(line) == 0 :
                if last >= i-2 :
                    last = i
                    lines.append (line)
                else :
                    skip += 1
            else :
                lines.append(line)
    if skip > 0 :
        with open(file,"w", encoding = encoding) as f :
            f.write("\n".join(lines))
            
def download_data ( name, 
                    moduleName  = None, 
                    url         = None, 
                    glo         = None, 
                    loc         = None,
                    whereTo     = ".",
                    website     = "xd",
                    fileprint   = print) :
    """
    retrieve a module given its name, a text file or a zip file,
    look for it on http://www.xavierdupre.fr/... (website),
    the file is copied at this file location and uncompressed if it is a zip file
    
    @param      name        (str) name of the module
    @param      moduleName  (str|None) like import name as moduleName, None for name
    @param      url         (str|None) link to the website to use
    @param      glo         (dict|None) if None, it will be replaced ``globals()``
    @param      loc         (dict|None) if None, it will be replaced ``locals()``
    @param      whereTo     specify a folder where downloaded files will be placed
    @param      website     website to look for
    @param      fileprint   logging function
    @return                 modules or list of files
    
    By extension, this function also download various zip files and decompresses it. 
    The following tools are available:
        - wscite.zip
        - gnuplot.exe.zip
        - ImageMagick-6.8.3-9-Q16-x86-windows.zip
        - _graphviz_draw.zip
        - SQLiteSpy.zip
        
    If the file was already downloaded, the function will not do it again.
    
    Example:
    @code
    from pyensae import download_data
    download_data('SQLiteSpy.zip', website = 'xd')
    @endcode
    """
    if glo == None : glo = globals()
    if loc == None : loc = locals()
    
    if website == "xd" :
        website = "http://www.xavierdupre.fr/enseignement/complements/"
    
    if not os.path.exists (whereTo) :
        raise Exception("this folder should exists " + whereTo)
        
    origname = name
    if name in sys.modules :
        return sys.modules[name]
    elif "." not in name :
        fileprint ("    unable to find module ", name)
    
    file    = name if "." in name else "%s.py" % name
    outfile = file if whereTo == "." else os.path.join( whereTo, file)

    if not os.path.exists (outfile) :
        path = "../../../../complements_site_web"
        f2 = os.path.join (path, file)
        if os.path.exists (f2) :
            fileprint ("adding file", f2)
            u = open (f2, "r")
            all = u.read ()
            u.close()
        else :
            if url == None : url = website
            url += file
            fileprint ("    downloading of ", url, " to ", outfile)
            if sys.version_info.major >= 3 :
                u = urllib.request.urlopen (url)
                all = u.read ()
                u.close ()
                u = open (outfile, "wb")
                u.write ( all )
                u.close()
            else :
                u = urllib2.urlopen (url, "r")
                all = u.read ()
                if "404 Not Found" in all and 'if "404 Not Found" in all :' not in all :
                    raise Exception ("fichier introuvable: " + name )
                u.close ()
                u = open (outfile, "wb" if ".exe" in file or ".zip" in file else "r")
                u.write ( all )
                u.close()
                
    if ".zip" in name :
        import zipfile
        file = zipfile.ZipFile (outfile, "r")
        files = []
        for info in file.infolist () :
            if not os.path.exists (info.filename) :
                data = file.read (info.filename)
                tos = os.path.join (whereTo, info.filename)
                if not os.path.exists (tos) :
                    finalfolder = os.path.split(tos)[0]
                    if not os.path.exists (finalfolder) :
                        fileprint ("    creating folder ", finalfolder)
                        os.makedirs (finalfolder)
                    if not info.filename.endswith ("/") :
                        u = open (tos, "wb")
                        u.write ( data )
                        u.close()
                        files.append (tos)
                        fileprint ("    unzipped ", info.filename, " to ", tos)
                elif not tos.endswith("/") :
                    files.append (tos)
            elif not info.filename.endswith ("/") :
                files.append (info.filename)
        return files
   
    elif "." not in name :
        path,filename = os.path.split(outfile)
        if filename != outfile :
            if path not in sys.path :
                sys.path.append (path)
            
        remove_empty_line(outfile)
        
        try :
            temp = importlib.import_module (name)
        except SystemError as e :
            if "Parent module '' not loaded" in str(e) :
                reg1 = re.compile("^(from +[.])[a-zA-Z]")
                reg2 = re.compile("^from +[.]{2}")
                fileprint("removing relative import for ", name)
                with open(outfile, "r") as f : lines = f.readlines()
                fil = [ ]
                fir = True
                for l in lines :
                    r1 = reg1.search(l)
                    r2 = reg2.search(l) 
                    if r2 :
                        l = ""
                        if fir: 
                            l = "HalLOG = print"
                            fir = False
                    elif r1 :
                        st = r1.groups()[0]
                        l = l.replace(st, "from ")
                        if fir: 
                            l += "\nHalLOG = print"
                            fir = False
                    fil.append(l.strip("\n\r"))
                if not fir:
                    fileprint("end removing relative import for ", name)
                    with open(outfile, "w") as f : f.write("\n".join(fil))
                    
            try :
                temp = importlib.import_module (name)
            except Exception as e :
                fileprint ("issue (3) while importing ", name, " -- ", origname)
                fileprint ("sys.path ", sys.path)
                for _ in sys.path : fileprint ("    path ", _)
                fileprint ("sys.modules.keys()", list(sys.modules.keys()))
                for _ in sorted(sys.modules) : fileprint ("    modules ", _)
                raise e
                
        except Exception as e :
            fileprint ("issue (2) while importing ", name, " -- ", origname)
            fileprint ("sys.path ", sys.path)
            for _ in sys.path : fileprint ("    path ", _)
            fileprint ("sys.modules.keys()", list(sys.modules.keys()))
            for _ in sorted(sys.modules) : fileprint ("    modules ", _)
            raise e
            
        if name not in temp.__name__ :
            raise Exception ("name should be present in __name__ " + name + " ? " + temp.__name__ )
        glo[moduleName] = temp
        sys.modules[moduleName] = temp
        sys.modules[origname] = temp
        return temp
        
    elif file.split(".")[-1] in ["txt", "csv", "tsv", "xml", "html"] :
        remove_empty_line(outfile)
        return outfile
    else :
        return outfile
    