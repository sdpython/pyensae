# -*- coding: utf-8 -*-
"""
@file
@brief Machine learning benchmark.
"""

from pyquickhelper.loghelper import noLOG
from pyquickhelper.benchhelper import BenchMark
from time import clock


class MlGridBenchMark(BenchMark):
    """
    Compares a couple of machine learning models.
    """

    def __init__(self, name, datasets, clog=None, fLOG=noLOG, path_to_images=".",
                 cache_file=None, **params):
        """
        initialisation

        @param      name            name of the test
        @param      datasets        list of dictionary of dataframes
        @param      clog            @see cl CustomLog or string
        @param      fLOG            logging function
        @param      params          extra parameters
        @param      path_to_images  path to images
        @param      cache_file      cache file

        If *cache_file* is specified, the class will store the results of the
        method @see me bench. On a second run, the function load the cache
        and run modified or new run (in *param_list*).

        *datasets* should be a dictionary with dataframes a values
        with the following keys:

        * ``'X'``: features
        * ``'Y'``: labels (optional)
        """
        BenchMark.__init__(self, name=name, datasets=datasets, clog=clog,
                           fLOG=fLOG, path_to_images=path_to_images,
                           cache_file=cache_file, **params)

        if not isinstance(datasets, list):
            raise TypeError("datasets must be a list")
        for i, df in enumerate(datasets):
            if not isinstance(df, dict):
                raise TypeError(
                    "Every dataset must be a dictionary, {0}th is not.".format(i))
            if "X" not in df:
                raise KeyError(
                    "Dictionary {0} should contain key 'X'.".format(i))
            if "di" in df:
                raise KeyError(
                    "Dictionary {0} should not contain key 'di'.".format(i))
            if "name" not in df:
                raise KeyError(
                    "Dictionary {0} should not contain key 'name'.".format(i))
            if "shortname" not in df:
                raise KeyError(
                    "Dictionary {0} should not contain key 'shortname'.".format(i))
        self._datasets = datasets
        self._results = []

    def init_main(self):
        """
        initialisation
        """
        self.fLOG("[MlGridBenchmark.init] begin")
        self._datasets_info = []
        for i, dd in enumerate(self._datasets):
            X = dd["X"]
            N = X.shape[0]
            Nc = X.shape[1]
            info = dict(Nrows=N, Nfeat=Nc)
            self.fLOG(
                "[MlGridBenchmark.init] dataset {0}: {1}".format(i, info))
            self._datasets_info.append(info)

        self.fLOG("[MlGridBenchmark.init] end")

    def init(self):
        """
        skip it
        """
        pass

    def run(self, params_list):
        """
        run the benchmark
        """
        self.init_main()
        self.fLOG("[MlGridBenchmark.bench] start")
        self.fLOG("[MlGridBenchmark.bench] number of datasets",
                  len(self._datasets))
        self.fLOG("[MlGridBenchmark.bench] number of experiments",
                  len(params_list))

        unique = set()
        for i, pars in enumerate(params_list):
            if "name" not in pars:
                raise KeyError(
                    "Dictionary {0} must contain key 'name'.".format(i))
            if "shortname" not in pars:
                raise KeyError(
                    "Dictionary {0} must contain key 'shortname'.".format(i))
            if pars["name"] in unique:
                raise ValueError("'{0}' is duplicated.".format(pars["name"]))
            unique.add(pars["name"])
            if pars["shortname"] in unique:
                raise ValueError(
                    "'{0}' is duplicated.".format(pars["shortname"]))
            unique.add(pars["shortname"])

        # Multiplies the experiments.
        full_list = []
        for i in range(len(self._datasets)):
            for pars in params_list:
                pc = pars.copy()
                pc["di"] = i
                full_list.append(pc)

        # Run the bench
        res = BenchMark.run(self, full_list)

        self.fLOG("[MlGridBenchmark.bench] end")
        return res

    def bench(self, **params):
        """
        run an experiment, parameter *di* is the dataset to use
        """
        p2 = params.copy()
        del p2["di"]
        ds = self._datasets[params["di"]]
        cl = clock()
        output = self.bench_experiment(ds, **p2)
        train = clock() - cl
        appe = self._datasets_info[params["di"]]
        metrics = self.score_experiment(ds, output)
        cl = clock()
        test = clock() - cl
        metrics["time_train"] = train
        metrics["time_test"] = test
        metrics[
            "_btry"] = "{0}-{1}".format(params["shortname"], ds["shortname"])
        metrics.update(appe)
        appe["_btry"] = metrics["_btry"]
        if "_i" in metrics:
            del metrics["_i"]
        return metrics, appe

    def bench_experiment(self, info, **params):
        """
        function to overload

        @param      info        dictionary with at least key ``'X'``
        @return                 output of the experiment
        """
        raise NotImplementedError()

    def score_experiment(self, info, output, **params):
        """
        function to overload

        @param      info        dictionary with at least key ``'X'``
        @return                 output of the experiment
        """
        raise NotImplementedError()
