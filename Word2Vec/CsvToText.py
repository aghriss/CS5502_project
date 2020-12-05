



from Word2Vec.FeatureExtractor import FeatureExtractor
from Word2Vec.FeatureExtractor import BigramExtractor
import pandas as pd

def getText(df, colName):
    text = ""
    for t in df[colName]:
        text += str(t)
    return text

def getTextAndDump(csvFile, outputFile):
    df = pd.read_csv(csvFile, error_bad_lines=False)
    text = getText(df, "text")
    f = open(outputFile, "w", encoding="utf-8")
    f.write(text)
    f.close()

csvFile = "Arizona.csv"
textFileName = "Arizon_text.txt"
getTextAndDump(csvFile, textFileName)

csvFilePop = "Arizona_popular.csv"
textFileNamePop = "Arizona_popular.txt"
getTextAndDump(csvFilePop, textFileNamePop)



fe = FeatureExtractor(textFileName, textFileNamePop)
features = fe.features

for f in features:
    print(f)


# featureExt = FeatureExtractor("alice.txt", "queen.txt")
# feat = featureExt.features
#
# biExt = BigramExtractor()
#
# s = "I like ice cream."
# bigrams = biExt.getBigrams(s)
# featuresOn = []
# for b in bigrams:
#     if b in feat:
#         featuresOn.append(b)
#     else:
#         print(f'{b} not present')
#
#
#
