



from Word2Vec.FeatureExtractor import FeatureExtractor
from Word2Vec.ApplyFeatures import ApplyFeatures
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




