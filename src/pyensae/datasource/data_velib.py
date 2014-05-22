#-*- coding:utf-8 -*-
"""
@file
@brief The file contains a class which collects data coming from Velib.

"""

import os, os.path, sys, datetime, urllib, json, time

class DataVelibCollect :
    """
    This class automates data collecting from Velib website.
    The service is provided at `JCDecaux developper <https://developer.jcdecaux.com/#/home>`_.
    
    see `notebook on Velib <http://nbviewer.ipython.org/5520933>`_
    
    The list of contracts for JCDecaux can obtained at:
    `Données statiques <https://developer.jcdecaux.com/#/opendata/vls?page=static>`_.
    
    The API provided by JCDecaux is described `here <https://developer.jcdecaux.com/#/opendata/vls?page=dynamic>`_.
    """

    #: list of available cities = contract
    _contracts_static = { k:1 for k in [ 'Arcueil',
                       'Besancon',
                       'Lyon',
                       'Paris',
                        ] }
                       
    # api: two substring to replace (contract, apiKey)
    _url_api  = "https://api.jcdecaux.com/vls/v1/stations?contract=%s&apiKey=%s"
    _url_apic = "https://api.jcdecaux.com/vls/v1/contracts?apiKey=%s"

    
    def __init__ (self, apiKey, fetch_contracts = False) :
        """
        constructor
        
        @param          apiKey              api key
        @param          fetch_contracts     if True, it uses a short list of known contracts,
                                            otherwise, it will updated through the website API
        """
        self.apiKey = apiKey
        self.contracts = DataVelibCollect._contracts_static if not fetch_contracts else self.get_contracts() 
        
        # sometimes, lng and lat are null, check if some past retreiving returned non null coordinates
        self.memoGeoStation = { }

    def get_contracts(self):
        """
        returns the list of contracts 
        
        @return     dictionary    { 'station':1 }
        """
        url = DataVelibCollect._url_apic % (self.apiKey)
        try :
            with urllib.request.urlopen(url) as u :
                js = u.read()
        except (urllib.error.HTTPError, urllib.error.URLError) as exc :
            # there was probably a mistake
            # We try again after a given amount of time
            time.sleep(0.5)
            try :
                with urllib.request.urlopen(url) as u :
                    js = u.read()
            except (urllib.error.HTTPError, urllib.error.URLError) as exc :
                # there was probably a mistake
                # we stop
                raise Exception("unable to access url: "+  url) from exc
        
        js = str(js, encoding="utf8")
        js = json.loads(js)
        cont = { k["name"]:1 for k in js }
        return cont
        
    def get_json (self, contract) :
        """
        return the data associated to a contract
        @param      contract        contract name, @see te _contracts
        @return                     json string
        """
        if contract not in self.contracts :
            raise Exception("unable to find contrat in:\n" + "\n".join(self.contracts.keys()))
        url = DataVelibCollect._url_api % (contract, self.apiKey)
        
        try :
            with urllib.request.urlopen(url) as u :
                js = u.read()
        except (urllib.error.HTTPError, urllib.error.URLError) as exc :
            # there was probably a mistake
            # We try again after a given amount of time
            time.sleep(0.5)
            try :
                with urllib.request.urlopen(url) as u :
                    js = u.read()
            except (urllib.error.HTTPError, urllib.error.URLError) as exc :
                # there was probably a mistake
                # we stop
                return json.loads("[]")
            
        js = str(js, encoding="utf8")
        js = json.loads(js)
        for o in js :
            o["number"]  = int(o["number"])
            o["banking"] = 1 if o["banking"] == "True" else 0
            o["bonus"]   = 1 if o["bonus"] == "True" else 0
            
            o["bike_stands"]            = int(o["bike_stands"])
            o["available_bike_stands"]  = int(o["available_bike_stands"])
            o["available_bikes"]        = int(o["available_bikes"])
            o["collect_date"]           = datetime.datetime.now()
            
            ds = float(o["last_update"])
            dt = datetime.datetime.fromtimestamp(ds/1000)
            o["last_update"] = dt
            
            try :
                o["lat"] = float(o["position"]["lat"]) if o["position"]["lat"] != None else None
                o["lng"] = float(o["position"]["lng"]) if o["position"]["lng"] != None else None
            except TypeError as e :
                raise TypeError ("unable to convert geocode for the following row: %s\n%s" % (str(o), str(e)))
                
            key = contract,o["number"]
            if key in self.memoGeoStation :
                if o["lat"] == 0 or o["lng"] == 0 :
                    o["lat"],o["lng"] = self.memoGeoStation [key]
            elif o["lat"] != 0 and o["lng"] != 0 :
                self.memoGeoStation [key] = o["lat"],o["lng"]
            
            del o["position"]
            
        return js
        
    def collecting_data (self, contract,
                               delayms          = 1000,
                               outfile          = "velib_data.txt",
                               single_file      = True,
                               stop_datetime    = None,
                               log_every        = 10,
                               fLOG             = print) :
        """
        collects data for a period of time
        @param      contract        contract name, @see te _contracts
        @param      delayms         delay between two collections (in ms)
        @param      outfile         write data in this file (json), if single_file is True, outfile is used as a prefix
        @param      single_file     True: one file, else, many files with timestamp as a suffix
        @param      stop_datetime   if None, never stops, else stops when the date is reached
        @param      log_every       print something every <log_every> times data were collected
        @param      fLOG            logging function
        @return                     list of created file
        """
        delay    = datetime.datetime.fromtimestamp(delayms/1000.0) - datetime.datetime.fromtimestamp(0.)
        now      = datetime.datetime.now()
        cloc     = now
        delayms /= 50 
        delays   = delayms / 1000.0
        
        nb = 0
        while stop_datetime == None or now < stop_datetime :
            now   = datetime.datetime.now()
            cloc += delay
            js  = self.get_json(contract)
            
            if single_file :
                with open(outfile, "a", encoding="utf8") as f :
                    f.write("%s\t%s\n" % (str(now), str(js)))
            else :
                name = outfile + "." + str(now).replace (":","-").replace ("/","-").replace (" ","_") + ".txt"
                with open(name, "w", encoding="utf8") as f :
                    f.write(str(js))
            
            nb += 1
            if nb % log_every == 0 : 
                fLOG ( "DataVelib.collecting_data: ", nb, " times: ", now, " delay = ", delay, "next", cloc, " delays ", delays)
            
            while now < cloc :
                now = datetime.datetime.now()
                time.sleep(delays)
                
    @staticmethod
    def run_collection (
                                key             = None,
                                contract        = "Paris",
                                delayms         = 60000,
                                folder_file     = "velib_data",
                                stop_datetime   = None,
                                single_file     = False,
                                log_every       = 1,
                                fLOG            = print) :
        """
        run the collection of the data for velib, data are stored using Json format.
        The function creates a file every time a new status is downloaded.
        
        @param      key             (str|None) if None, the function calls function @see fn velib_get_key
        @param      contract        a city
        @param      delayms         gets a status every delayms milliseconds
        @param      folder_file     prefix used to create one file or several, it depends on single_file) where to place downloaded files)   
        @param      stop_datetime   (datetime) stop when this datetime is reached or None for never stops
        @param      single_file     if True, every json status will be stored in a single file, if False, it will be 
                                    a different file each time, if True, then folder_file is a file
        @param      log_every       log some information every 1 (minutes)
        @param      fLOG            logging function
        
        @example(collect Velib data)
        The following example produces a file every minute in json format about the status of all
        Velib stations in Paris. They will be put in a folder call ``velib_data``.
        @code
        DataVelibCollect.run_collection (private_key,
                    contract = "Paris",
                    delayms = 60000,
                    single_file = False,
                    stop_datetime = None, 
                    log_every = 1)        
        @endcode
        
        @endexample
        """
        if key == None :
            key = DataVelibCollect.velib_get_key()
        velib = DataVelibCollect(key, True)
        velib.collecting_data ( contract, 
                                delayms, 
                                folder_file, 
                                stop_datetime = stop_datetime, 
                                single_file = single_file,
                                log_every = log_every,
                                fLOG = fLOG)
                
    def velib_get_key() :
        """
        open a windows to get a key (from a user) and a contract (city)
        the function is independent from the others
        
        @return     key
        """
        from pyquickhelper import open_window_params
        para =  { "velib_key": "" }
        para = open_window_params (para, DataVelibCollect.__doc__, "Velib Study")
        return None if "__cancel__" in para else para["velib_key"]            
