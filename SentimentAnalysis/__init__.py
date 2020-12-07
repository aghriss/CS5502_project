#from .text_process import cleanup
from .sentiment_features import NLP_features


from bs4 import BeautifulSoup
import emoji
import re 

from .dicts import load_dict_contractions, load_dict_smileys
from nltk.tokenize import WordPunctTokenizer

CONTRACTIONS = load_dict_contractions()
SMILEY = load_dict_smileys()



def cleanup(text):
    # HTML decoding
    soup = BeautifulSoup(text, 'lxml')
    # @ tag replace
    result = re.sub(r'@[A-Za-z0-9]+','',soup.getText())
    # remove URL
    result = re.sub(r'https?://[A-Za-z0-9./]+','',result)
    
    result = result.replace("’","'")
    
    #CONTRACTIONS source: https://en.wikipedia.org/wiki/Contraction_%28grammar%29
    words = result.split()
    reformed = [CONTRACTIONS[word] if word in CONTRACTIONS else word for word in words]
    result = " ".join(reformed)

    #Deal with emoticons source: https://en.wikipedia.org/wiki/List_of_emoticons
    words = result.split()
    reformed = [SMILEY[word] if word in SMILEY else word for word in words]
    result = " ".join(reformed)
    
    #Deal with emojis
    result = emoji.demojize(result)
    
    # remove non-alphabetical letter
    #result = re.sub("[^a-zA-Z]", " ", result)
    
    # remove unnecessary white spaces
    tok = WordPunctTokenizer()
    words = tok.tokenize(result)
    # remove stopwords
    #words = [word for word in words if not word in all_stopwords]
    
    return (" ".join(words)).strip()