from typing import List
from typing import Dict
from Series import  *
from Exceptions import WrongSeriesLengths

# TODO: Performance optimization.
# 1) If there are many Series in one DataFrame, we can write custom trie-like structure that would reduce space and
# search for a specific Series.
class DataFrame:
    def __init__(self, dicSeries: Dict[str, Series]):
        series_len = []
        for series in dicSeries.values():
            series_len.append(series.get_length())

        if series_len != 0:
            length = series_len[0]
        for ser_len in series_len:
            if length != ser_len:
                raise WrongSeriesLengths()

        self.set_dic_series(dicSeries)

    def set_dic_series(self, dicSeries: [str, Series]):
        self.dicSeries = dicSeries

    def get_dic_series(self):
        return self.dicSeries

    def get_num_rows(self):
        if len(self.get_dic_series()) == 0:
            return 0
        firstSeries = list(self.get_dic_series().values())[0]
        return firstSeries.get_length()

    def __getitem__(self, name):
        if type(name) is str:
            return self.get_dic_series()[name]
        elif type(name) is SeriesBool:
            dicOut = {}
            for key in self.get_dic_series().keys():
                dicOut[key] = self.get_dic_series()[key][name]
            return DataFrame(dicOut)
        else:
            raise WrongIndexType(name)

    def __str__(self):
        sOut = ""
        for series in self.get_dic_series().values():
            sOut += series.get_name() + " " + series.get_type_name() + ","
        sOut = sOut.removesuffix(",")
        sOut += "\n"
        for i in range(0, self.get_num_rows()):
            sOut += str(i) + " "
            for series in self.get_dic_series().values():
                sOut += str(series[i]) + " "
            sOut += "\n"
        return sOut
