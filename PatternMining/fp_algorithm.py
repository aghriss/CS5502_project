
import pyfpgrowth
import pandas as pd
import string
df = pd.read_csv("merged_data.csv",index_col=0)

import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
printable = set(string.printable)

df.text = df.text.fillna("")

def unicode(text):
    return "".join([t for t in text if t in printable])


def remove_punct(text):
    punct = '''!()-[]{};:'"\, <>./?@#क$%^&*_~…'ी'ा1234567890'''
    for p in punct:
        text = text.replace(p," ")
    return text.replace("  "," ").lower()

def remove_easy_words(text):
    words = ["and", "the", "to", "i", "with", "my", "is", "of", "it", "i", "be", "l", "ar", "ra", "you", "de", 'this', 'naughty'
             'st', 'com'] + [" "+c+" " for c in "abcdefghijklmnopqrstuvwxyz"]
    for w in words:
        text = text.replace(w," ")
    return text

df.text = df.text.map(unicode)
df.text = df.text.map(remove_punct)
#df.text = df.text.map(remove_easy_words)

text = "\n".join(list(df.text))


text = text.replace('''!()-[]{};:'"\, <>./?@#$%^&*_~''', " ")
words = ["and", "the", "to", "i", "with", "my", "is", "of", "it", "i", "be", "l", "ar", "ra", "you", "de", 'this', 'naughty', 'he',
         'th','for','in', 'on','la','he','was','but','will','we','but','a','so','no',
             'st', 'com'] + [" "+c+" " for c in "0123456789abcdefghijklmnopqrstuvwxyz"]
   
tweets = list(df.text.fillna("")[df.trending==0])
token = nltk.word_tokenize(text)
token = list(filter(lambda x : x.lower() not in words, token))
unigrams = dict(nltk.FreqDist((ngrams(token,1))))
lst = list(unigrams.items())
lst.sort(key=lambda x: -x[1])
lst_index = {v[0]:k for k,v in enumerate(lst)}
lst_reverse = {k:v[0] for k,v in enumerate(lst)}

def text_to_items(text):
    text = text.replace('''!()-[]{};:'"\, <>./?@#$%^&*_~''', " ")
    tokens = list(ngrams(nltk.word_tokenize(text),1))
    items = [lst_index[t] for t in tokens if t in lst_index]
    return sorted(items)[:min(10,len(items))]
    
res = list( map(text_to_items, tweets))

bigrams = ngrams(token,3)



patterns = pyfpgrowth.find_frequent_patterns(res, 40)
rules = pyfpgrowth.generate_association_rules(patterns, 0.7)

def reverse_rule(rule):
    return [lst_reverse[r] for r in rule]

reverse = [(reverse_rule(r),rules[r]) for r in rules]
print(reverse)


list(sorted(reverse, key=lambda x: -x[1][1]))[:50]
