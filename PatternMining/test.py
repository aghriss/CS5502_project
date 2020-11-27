
import configparser
import pickle
import pandas as pd

config = configparser.ConfigParser()
config.read('../_config.ini')

normNotSplitFile = "." + config["NormData"]["NotSplit"]

def ReadData(fileName):
    data = pickle.load(open(fileName,"rb"))
    xAll = data[0]
    yAll = data[1]
    return xAll, yAll


xAll, yAll = ReadData(normNotSplitFile)

with pd.option_context( 'display.max_columns', None):  # more options can be specified also
    print(xAll)