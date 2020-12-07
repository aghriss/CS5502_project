


from Word2Vec.FeatureExtractor import BigramExtractor
import pandas as pd
import pickle


class ApplyFeatures:
    def __init__(self, featureFile, csvFile, colName):
        self.df = self.applyFeatures(featureFile, csvFile, colName)

    def getFeaturesOn(self, s, features):
        biExt = BigramExtractor()
        bigrams = biExt.getBigrams(s)
        featuresOn = []
        for b in bigrams:
            if b in features:
                featuresOn.append(b)

        return featuresOn


    def applyFeatures(self, featureFile, csvFile, colName):
        features = pickle.load(open(featureFile, "rb"))
        df = pd.read_csv(csvFile, error_bad_lines=False)

        for f in features:
            df[f] = 0

        for i, t in enumerate(df[colName]):
            featFound = self.getFeaturesOn(str(t), features)
            for f in featFound:
                df[f][i] = 1

        df = df.drop(columns=[colName])
        # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        #     print(df)

        return df