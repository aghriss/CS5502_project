



from Word2Vec.FeatureExtractor import FeatureExtractor
from Word2Vec.FeatureExtractor import BigramExtractor
import pandas as pd
import pickle

class DumpText():
    def __init__(self, csvFile, textFile, colName):
        self.getTextAndDump(csvFile, textFile, colName)

    def getText(self, df, colName):
        text = ""
        for t in df[colName]:
            text += str(t)
        return text

    def getTextAndDump(self, csvFile, outputFile, colName):
        df = pd.read_csv(csvFile, error_bad_lines=False)
        text = self.getText(df, colName)
        f = open(outputFile, "w", encoding="utf-8")
        f.write(text)
        f.close()


def DumpPickle(fileName, data):
    with open(fileName, "wb") as handle:
        pickle.dump(data, handle)


def DumpFeatures(csvFile, textFileName, csvFilePop, textFileNamePop, featureFile, colName, compareTop, limit):
    DumpText(csvFile, textFileName, colName)
    DumpText(csvFilePop, textFileNamePop, colName)
    fe = FeatureExtractor(textFileName, textFileNamePop, compareTop, limit)
    features = fe.features
    DumpPickle(featureFile, features)


def getFeaturesOn(s, features):
    biExt = BigramExtractor()
    bigrams = biExt.getBigrams(s)
    featuresOn = []
    for b in bigrams:
        if b in features:
            featuresOn.append(b)

    return featuresOn


def applyFeatures(featureFile, csvFile, colName):
    features = pickle.load(open(featureFile, "rb"))
    df = pd.read_csv(csvFile, error_bad_lines=False)

    for f in features:
        df[f] = 0

    for i, t in enumerate(df[colName]):
        featFound = getFeaturesOn(str(t), features)
        for f in featFound:
            df[f][i] = 1

    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(df)

    return df


# Need csvFile and csvFilePop to get started
csvFile = "Arizona.csv"
textFileName = "Arizon_text.txt"
csvFilePop = "Arizona_popular.csv"
textFileNamePop = "Arizona_popular.txt"
featureFile = "Arizona_feature.p"
featurizedFile = "featurized_Arizona.p"
colName = "text"

# Get a list of features and dump them in a pickle file
DumpFeatures(csvFile, textFileName, csvFilePop, textFileNamePop, featureFile, colName, 700, 100)

# Apply the new features to the df
df = applyFeatures(featureFile, csvFile, colName)

# Save the new df
DumpPickle(featurizedFile, df)
