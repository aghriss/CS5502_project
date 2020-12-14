import nltk 

# Extract bigrams from the sentences
def extract_bigrams_from_corpus(sentences):
    #sample = open(fileName, "r", encoding="utf8")
    s =sentences# sample.read()    
    tokens = nltk.word_tokenize(s)
    bgs = nltk.bigrams(tokens)
    fdist = nltk.FreqDist(bgs)

    d = dict(fdist)
    lst = list(d.items())
    lst.sort(key=lambda x: -x[1])
    
    
    sorted_bigrams = list(dict(lst).keys())
    sorted_dict = {k:v for v,k in enumerate(sorted_bigrams)}
    for bigram in d.keys():
        d[bigram] = (d[bigram],sorted_dict[bigram])
        
        
    return d

# Extract bigrams and put them in a sorted list
def extract_bigrams_from_text(text):
    tokens = nltk.word_tokenize(text)
    bgs = nltk.bigrams(tokens)
    fdist = nltk.FreqDist(bgs)

    d = dict(fdist)
    lst = list(d.items())
    lst.sort(key=lambda x: -x[1])
    return  d

# Get unique features from the bigrams extracted
def getUniqFeat(bigrams_text, bigrams_file, limit):

    frequency = []
    for bigram in bigrams_text:
        if bigram in bigrams_file:
            frequency.append(bigrams_file[bigram])
        else:
            frequency.append((0, len(bigrams_file)+1))
            
    frequency.sort(key=lambda x: -x[0])
    return [x[1] for x in (frequency[:min(len(frequency), limit)] + 
                           [(-1,-1)]*(limit-len(frequency)))]

