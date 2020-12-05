
import warnings
import nltk

warnings.filterwarnings(action='ignore')


# Get a list of bigrams sorted by their frequency
# [("I", "am"), ("to", "the"), ...]
def getBigrams(s):
    tokens = nltk.word_tokenize(s)
    bgs = nltk.bigrams(tokens)
    fdist = nltk.FreqDist(bgs)

    d = dict(fdist)
    lst = list(d.items())
    lst.sort(key=lambda x:x[1], reverse=True)

    return list(dict(lst).keys())

# Wrapper for the previous function
# Read the file and return bigrams
def getBigramsFromFile(fileName):
    sample = open(fileName, "r", encoding="utf8")
    s = sample.read()
    return getBigrams(s)


# It goes through top (compareTop) elements in the bigrams1 list
# If the item is not found in the top (compareTop) of bigrams2, it's added to the list
# This would mean that the item is common in bigrams1, but not in bigrams2 so it can be a good feature
def getUniqFeat(bigrams1, bigrams2, compareTop, limit):
    features = []
    for indX in range(compareTop):
        x = bigrams1[indX]
        indY = len(bigrams2)
        try:
            indY = bigrams2.index(x)
        except:
            pass

        if indY > compareTop:
            features.append(x)

        if len(features) == limit:
            return features
    return features



bigrams1 = getBigramsFromFile("alice.txt")
bigrams2 = getBigramsFromFile("queen.txt")
compareTop = 700
numFeats = 100

feat = getUniqFeat(bigrams1, bigrams2, compareTop, numFeats / 2)
feat += getUniqFeat(bigrams2, bigrams1, compareTop, numFeats / 2)

# for i, f in enumerate(feat):
#     print(f'{i}: {f}')

feat = set(feat)



# CSV to text
# row + features = features on


s = "I like ice cream."
bigrams = getBigrams(s)
for b in bigrams:
    if b in feat:
        print(b)
    else:
        print(f'{b} not present')
