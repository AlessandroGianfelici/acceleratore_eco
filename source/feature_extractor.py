import pandas as pd
import logging
from functools import reduce, partial
from operator import add
import numpy as np
import os
import pandas as pd
import plotly.express as px
logger = logging.getLogger("__main__")


class FeatureExtraxtor(object):

    def __init__(self, worldbank_data, global_economic_indicators):
        self._worldbank_data = worldbank_data
        self._global_economic_indicators = global_economic_indicators
        return

    def get_groundtruth(self):
        return 

    def compute_features(self):
        return

    def mergeFeatures(self, data_frames, index):
        """
        This method take as input a list of dataframes and return their outer join on the column 'Accident_Index'.
        """
        return reduce(lambda left, right: pd.merge(left,right,on=index, how='outer'), data_frames)