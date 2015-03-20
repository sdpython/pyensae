#-*- coding:utf-8 -*-
"""
@file
@brief The file contains a class which collects data coming from Velib.

"""

import os
import os.path
import datetime
import urllib
import json
import time
import re
import pandas
import numpy
import math
import random
import urllib.error
import urllib.request


class DataVelibCollect:

    """
    This class automates data collecting from Velib website.
    The service is provided at `JCDecaux developer <https://developer.jcdecaux.com/#/home>`_.

    see `notebook on Velib <http://nbviewer.ipython.org/5520933>`_

    The list of contracts for JCDecaux can obtained at:
    `Données statiques <https://developer.jcdecaux.com/#/opendata/vls?page=static>`_.

    The API provided by JCDecaux is described `here <https://developer.jcdecaux.com/#/opendata/vls?page=dynamic>`_.
    """

    #: list of available cities = contract
    _contracts_static = {k: 1 for k in ['Arcueil',
                                        'Besancon',
                                        'Lyon',
                                        'Paris',
                                        ]}

    # api: two substring to replace (contract, apiKey)
    _url_api = "https://api.jcdecaux.com/vls/v1/stations?contract=%s&apiKey=%s"
    _url_apic = "https://api.jcdecaux.com/vls/v1/contracts?apiKey=%s"

    def __init__(self, apiKey, fetch_contracts=False):
        """
        constructor

        @param          apiKey              api key
        @param          fetch_contracts     if True, it uses a short list of known contracts,
                                            otherwise, it will updated through the website API
        """
        self.apiKey = apiKey
        self.contracts = DataVelibCollect._contracts_static if not fetch_contracts else self.get_contracts()

        # sometimes, lng and lat are null, check if some past retrieving
        # returned non null coordinates
        self.memoGeoStation = {}

    def get_contracts(self):
        """
        returns the list of contracts

        @return     dictionary    { 'station':1 }
        """
        url = DataVelibCollect._url_apic % (self.apiKey)
        try:
            with urllib.request.urlopen(url) as u:
                js = u.read()
        except (urllib.error.HTTPError, urllib.error.URLError) as exc:
            # there was probably a mistake
            # We try again after a given amount of time
            time.sleep(0.5)
            try:
                with urllib.request.urlopen(url) as u:
                    js = u.read()
            except (urllib.error.HTTPError, urllib.error.URLError) as exc:
                # there was probably a mistake
                # we stop
                raise Exception("unable to access url: " + url) from exc

        js = str(js, encoding="utf8")
        js = json.loads(js)
        cont = {k["name"]: 1 for k in js}
        return cont

    def get_json(self, contract):
        """
        return the data associated to a contract
        @param      contract        contract name, @see te _contracts
        @return                     json string
        """
        if contract not in self.contracts:
            raise Exception(
                "unable to find contract in:\n" +
                "\n".join(
                    self.contracts.keys()))
        url = DataVelibCollect._url_api % (contract, self.apiKey)

        try:
            with urllib.request.urlopen(url) as u:
                js = u.read()
        except (urllib.error.HTTPError, urllib.error.URLError):
            # there was probably a mistake
            # We try again after a given amount of time
            time.sleep(0.5)
            try:
                with urllib.request.urlopen(url) as u:
                    js = u.read()
            except (urllib.error.HTTPError, urllib.error.URLError):
                # there was probably a mistake
                # we stop
                return json.loads("[]")

        js = str(js, encoding="utf8")
        js = json.loads(js)
        now = datetime.datetime.now()
        for o in js:
            o["number"] = int(o["number"])
            o["banking"] = 1 if o["banking"] == "True" else 0
            o["bonus"] = 1 if o["bonus"] == "True" else 0

            o["bike_stands"] = int(o["bike_stands"])
            o["available_bike_stands"] = int(o["available_bike_stands"])
            o["available_bikes"] = int(o["available_bikes"])
            o["collect_date"] = now

            try:
                ds = float(o["last_update"])
                dt = datetime.datetime.fromtimestamp(ds / 1000)
            except ValueError:
                dt = datetime.datetime.now()
            except TypeError:
                dt = datetime.datetime.now()
            o["last_update"] = dt

            try:
                o["lat"] = float(
                    o["position"]["lat"]) if o["position"]["lat"] is not None else None
                o["lng"] = float(
                    o["position"]["lng"]) if o["position"]["lng"] is not None else None
            except TypeError as e:
                raise TypeError(
                    "unable to convert geocode for the following row: %s\n%s" %
                    (str(o), str(e)))

            key = contract, o["number"]
            if key in self.memoGeoStation:
                if o["lat"] == 0 or o["lng"] == 0:
                    o["lat"], o["lng"] = self.memoGeoStation[key]
            elif o["lat"] != 0 and o["lng"] != 0:
                self.memoGeoStation[key] = o["lat"], o["lng"]

            del o["position"]

        return js

    def collecting_data(self, contract,
                        delayms=1000,
                        outfile="velib_data.txt",
                        single_file=True,
                        stop_datetime=None,
                        log_every=10,
                        fLOG=print):
        """
        collects data for a period of time
        @param      contract        contract name, @see te _contracts
        @param      delayms         delay between two collections (in ms)
        @param      outfile         write data in this file (json), if single_file is True, outfile is used as a prefix
        @param      single_file     if True, one file, else, many files with timestamp as a suffix
        @param      stop_datetime   if None, never stops, else stops when the date is reached
        @param      log_every       print something every <log_every> times data were collected
        @param      fLOG            logging function
        @return                     list of created file
        """
        delay = datetime.datetime.fromtimestamp(
            delayms / 1000.0) - datetime.datetime.fromtimestamp(0.)
        now = datetime.datetime.now()
        cloc = now
        delayms /= 50
        delays = delayms / 1000.0

        nb = 0
        while stop_datetime is None or now < stop_datetime:
            now = datetime.datetime.now()
            cloc += delay
            js = self.get_json(contract)

            if single_file:
                with open(outfile, "a", encoding="utf8") as f:
                    f.write("%s\t%s\n" % (str(now), str(js)))
            else:
                name = outfile + "." + \
                    str(now).replace(":",
                                     "-").replace("/",
                                                  "-").replace(" ",
                                                               "_") + ".txt"
                with open(name, "w", encoding="utf8") as f:
                    f.write(str(js))

            nb += 1
            if nb % log_every == 0:
                fLOG(
                    "DataVelib.collecting_data: ",
                    nb,
                    " times: ",
                    now,
                    " delay = ",
                    delay,
                    "next",
                    cloc,
                    " delays ",
                    delays)

            while now < cloc:
                now = datetime.datetime.now()
                time.sleep(delays)

    @staticmethod
    def run_collection(
            key=None,
            contract="Paris",
            delayms=60000,
            folder_file="velib_data",
            stop_datetime=None,
            single_file=False,
            log_every=1,
            fLOG=print):
        """
        run the collection of the data for velib, data are stored using Json format.
        The function creates a file every time a new status is downloaded.

        @param      key             (str|None) if None, the function calls function see @see me velib_get_key
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
        if key is None:
            key = DataVelibCollect.velib_get_key()
        velib = DataVelibCollect(key, True)
        velib.collecting_data(contract,
                              delayms,
                              folder_file,
                              stop_datetime=stop_datetime,
                              single_file=single_file,
                              log_every=log_every,
                              fLOG=fLOG)

    @staticmethod
    def velib_get_key():
        """
        open a windows to get a key (from a user) and a contract (city)
        the function is independent from the others

        @return     key
        """
        from pyquickhelper import open_window_params
        para = {"velib_key": ""}
        para = open_window_params(
            para,
            DataVelibCollect.__doc__,
            "Velib Study")
        return None if "__cancel__" in para else para["velib_key"]

    @staticmethod
    def to_df(folder, regex="velib_data.*[.]txt"):
        """
        reads all file in a folder (assuming there were produced by this class) and
        returns a dataframe with it

        each file is a status of all stations, a row per station will be added to the file

        @param  folder      folder where to find the files
        @param  regex       regular expression which filter the files
        @return             pandas DataFrame

        It produces a table with the following columns:
            - address
            - available_bike_stands
            - available_bikes
            - banking
            - bike_stands
            - bonus
            - collect_date
            - contract_name
            - last_update
            - lat
            - lng
            - name
            - number
            - status
            - file
        """
        if regex is None:
            regex = ".*"
        reg = re.compile(regex)

        files_ = os.listdir(folder)
        files = [_ for _ in files_ if reg.search(_)]

        if len(files) == 0:
            raise FileNotFoundError(
                "no found files in directory: " +
                folder +
                "\nregex: " +
                regex)

        rows = []
        for file_ in files:
            file = os.path.join(folder, file_)
            with open(file, "r", encoding="utf8") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                dl = eval(line.strip("\n\r\t "))
                if not isinstance(dl, list):
                    raise TypeError(
                        "we expect a list for line {0} in file {1}".format(
                            i,
                            file))
                for d in dl:
                    d["file"] = file_
                rows.extend(dl)

        return pandas.DataFrame(rows)

    @staticmethod
    def draw(df, **args):
        """
        draw a graph using four columns: lng, lat, available_bike_stands, available_bikes

        @param      args                other parameters to give method ``plt.subplots``
        @return                         fig, ax, plt, (fig,ax) comes plt.subplot, plt is matplotlib.pyplot
        """
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(**args)

        x = df["lng"]
        y = df["lat"]
        areaf = df.apply(
            lambda r: numpy.pi * (r["available_bike_stands"]) ** 2, axis=1)
        areab = df.apply(
            lambda r: numpy.pi * (r["available_bikes"]) ** 2, axis=1)
        ax.scatter(x, y, areaf, alpha=0.5, label="place", color="r")
        ax.scatter(x, y, areab, alpha=0.5, label="bike", color="g")
        ax.grid(True)
        ax.legend()
        ax.set_xlabel("longitude")
        ax.set_ylabel("latitude")

        return fig, ax, plt

    @staticmethod
    def js_animation(df, interval=20, **args):
        """
        This function uses the module `JSAnimation <https://github.com/jakevdp/JSAnimation>`_.
        To install it, you can run:

        @code
        try :
            from JSAnimation import IPython_display
        except ImportError:
            import pymyinstall
            pymyinstall.ModuleInstall("JSAnimation", "github", "jakevdp").install(temp_folder="c:\\temp")
            # an error does not mean necessarily the installation failed
        @endcode

        @param      interval            see `animation.FuncAnimation <http://matplotlib.org/api/animation_api.html#matplotlib.animation.FuncAnimation>`_
        @param      args                other parameters to give method ``plt.figure``
        @return                         animation

        It does not work very well for the time being.
        """

        #from JSAnimation import IPython_display
        import matplotlib.pyplot as plt
        from matplotlib import animation

        #xlim = min(df["lng"]),max(df["lng"])
        #ylim = min(df["lat"]),max(df["lat"])

        dates = list(sorted(set(df["file"])))
        datas = []
        for d in dates:
            sub = df[df["file"] == d]
            x = sub["lng"]
            y = sub["lat"]
            colp = df.apply(
                lambda r: numpy.pi * (r["available_bike_stands"]) ** 2, axis=1)
            colb = df.apply(
                lambda r: numpy.pi * (r["available_bikes"]) ** 2, axis=1)
            x = tuple(x)
            y = tuple(y)
            colp = tuple(colp)
            colb = tuple(colb)
            data = (x, y, colp, colb)
            datas.append(data)

        fig, ax = plt.subplots(**args)
        x, y, c, d = datas[0]

        scat1 = ax.scatter(x, y, c, alpha=0.5, color="r", label="place")
        scat2 = ax.scatter(x, y, d, alpha=0.5, color="g", label="bike")
        ax.grid(True)
        ax.legend()
        ax.set_xlabel("longitude")
        ax.set_ylabel("latitude")

        def animate(i, datas, scat1, scat2):
            x, y, c, d = datas[i]
            # scat1.set_array(numpy.array(c))
            # scat2.set_array(numpy.array(d))
            #scat1.set_array(numpy.array(x + y))
            #scat2.set_array(numpy.array(x + y))
            scat1._sizes = c
            scat2._sizes = d
            return scat1, scat2

        anim = animation.FuncAnimation(fig, animate, frames=len(datas),
                                       interval=interval, fargs=(datas, scat1, scat2), blit=True)
        plt.close('all')
        return anim

    @staticmethod
    def distance_haversine(lat1, lon1, lat2, lon2):
        """
        compute the haversine distance

        see `Haversine distance <http://en.wikipedia.org/wiki/Haversine_formula>`_

        @return      double
        """
        radius = 6371
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c
        return d

    @staticmethod
    def simulate(df, nbbike, speed,
                 period=datetime.timedelta(minutes=1),
                 iteration=500,
                 min_min=10,
                 delta_speed=2.5,
                 fLOG=print):
        """
        simulate velibs on a set of stations given by df

        @param      nbbike      number of bicycles
        @param      period      period
        @param      speed       average speed (in km/h)
        @param      iteration   number of iterations
        @param      min_min     minimum duration of a trip
        @param      delta_speed allowed speed difference
        @param      fLOG        logging function
        @return                 simulated paths, data (as DataFrame)
        """
        cities = df[["lat", "lng", "name", "number"]]
        start = cities.drop_duplicates()
        idvelo = 0

        current = {}
        for row in start.values:
            r = []
            for i in range(0, 5):
                r.append(idvelo)
                idvelo += 1
            r.extend([-1, -1, -1, -1, -1])
            ids = tuple(row)
            current[ids] = r

        running = []

        def free(v):
            nb = [_ for _ in v if _ == -1]
            return len(nb) > 0

        def bike(v):
            nb = [_ for _ in v if _ == -1]
            return len(nb) < len(v)

        def pop(v):
            for i, _ in enumerate(v):
                if _ != -1:
                    r = v[i]
                    v[i] = -1
                    fLOG("    pop", v)
                    return r
            raise Exception("no free bike")

        def push(v, idv):
            for i, _ in enumerate(v):
                if _ == -1:
                    v[i] = idv
                    fLOG("    push", v)
                    return None
            raise Exception("no free spot: " + str(v))

        def give_status(conf, time):
            rows = []
            for k, v in conf.items():
                lat, lng, name, number = k
                obs = {"lat": lat, "lng": lng, "name": name, "number": number}
                nb = [_ for _ in v if _ == -1]
                obs["available_bike_stands"] = len(nb)
                obs["available_bikes"] = len(v) - len(nb)
                obs["collect_date"] = time
                obs["file"] = str(time)
                rows.append(obs)
            return rows

        simulation = []
        paths = []
        keys = list(current.keys())
        iter = 0
        time = datetime.datetime.now()
        while iter < iteration:

            status = give_status(current, time)
            simulation.extend(status)

            # a bike
            if len(running) < nbbike:
                rnd = random.randint(0, len(keys) - 1)
                v = current[keys[rnd]]
                if bike(v):
                    v = (time, pop(v), keys[rnd], "begin")
                    running.append(v)
                    lat, lng, name, number = keys[rnd]
                    dv = {
                        "lat0": lat,
                        "lng0": lng,
                        "name0": name,
                        "number0": number}
                    dv.update({"time": v[0],
                               "idvelo": v[1],
                               "beginend": v[-1],
                               "hours": 0.0,
                               "dist": 0.0})
                    paths.append(dv)

            # do we put the bike back
            rem = []
            for i, r in enumerate(running):
                delta = time - r[0]
                h = delta.total_seconds() / 3600
                if h * 60 > min_min:
                    for rowi in cities.values:
                        row = cities.values[random.randint(0, len(cities) - 1)]
                        keycity = tuple(row)
                        station = current[keycity]
                        if free(station):
                            vlat, vlng = r[2][0], r[2][1]
                            clat, clng = row[0], row[1]
                            dist = DataVelibCollect.distance_haversine(
                                vlat,
                                vlng,
                                clat,
                                clng)
                            sp = dist / h
                            dsp = abs(sp - speed)
                            if (dsp < delta_speed or (sp < speed and h >= 1)) \
                                    and random.randint(0, 10) == 0:
                                # we put it back
                                push(station, r[1])
                                rem.append(i)

                                lat, lng, name, number = r[2]
                                dv = {
                                    "lat0": lat,
                                    "lng0": lng,
                                    "name0": name,
                                    "number0": number}
                                lat, lng, name, number = keycity
                                dv.update({"lat1": lat,
                                           "lng1": lng,
                                           "name1": name,
                                           "number1": number})
                                dv.update({"time": time,
                                           "idvelo": r[1],
                                           "beginend": "end",
                                           "hours": h,
                                           "dist": dist})
                                paths.append(dv)
                                break

            running = [r for i, r in enumerate(running) if i not in rem]

            fLOG(
                iter,
                "time ",
                time,
                " - ",
                len(running),
                "/",
                nbbike,
                " paths ",
                len(paths))

            # end of loop
            time += period
            iter += 1

        return pandas.DataFrame(paths), pandas.DataFrame(simulation)
