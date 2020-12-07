
import configparser
import pickle

from Word2Vec.CsvToText import DumpText
from Word2Vec.FeatureExtractor import FeatureExtractor
from Word2Vec.ApplyFeatures import ApplyFeatures

config = configparser.ConfigParser()
config.read('./_config.ini')

fileNames = config["RawData"]["FileNames"].split(", ")

def DumpPickle(fileName, data):
    with open(fileName, "wb") as handle:
        pickle.dump(data, handle)

def DumpFeatures(csvFile, textFileName, csvFilePop, textFileNamePop, featureFile, colName, compareTop, limit):
    DumpText(csvFile, textFileName, colName)
    DumpText(csvFilePop, textFileNamePop, colName)
    fe = FeatureExtractor(textFileName, textFileNamePop, compareTop, limit)
    features = fe.features
    DumpPickle(featureFile, features)




prefix = "./Data/"
for f in fileNames:
    csvFile = prefix + f + ".csv"
    textFileName = prefix + f + ".txt"
    csvFilePop = prefix + f + "_popular.csv"
    textFileNamePop = prefix + f + "_popular.txt"
    featureFile = prefix + f + "_feature.p"
    featurizedFile = prefix + f + "_featurized.p"
    colName = "text"

    print([csvFile, textFileName, csvFilePop, textFileNamePop, featureFile, featurizedFile])

    # Get a list of features and dump them in a pickle file
    DumpFeatures(csvFile, textFileName, csvFilePop, textFileNamePop, featureFile, colName, 700, 100)

    # Apply the new features to the df
    apFeat = ApplyFeatures(featureFile, csvFile, colName)
    df = apFeat.df

    # Save the new df
    DumpPickle(featurizedFile, df)
