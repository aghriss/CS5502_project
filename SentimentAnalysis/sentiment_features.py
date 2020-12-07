import flair
from flair.data import Sentence
from textblob import TextBlob

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



class NLP_features:
    flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
    flair_fast = flair.models.TextClassifier.load('sentiment-fast')
    sid = SentimentIntensityAnalyzer()
    
    def get_features(self, text):
        result ={}
        result.update(self.get_flair(text))
        result.update(self.get_flair_fast(text))
        result.update(self.get_textblob(text))
        result.update(self.get_vader(text))
        return result
    
    def get_flair(self, text):
        if len(text) == 0:
            return {"flair_sentiment": -1}
        s = Sentence(text)
        self.flair_sentiment.predict(s)
        total_sentiment = s.labels

        sign = -2*(total_sentiment[0].value=="NEGATIVE")+1.0
        
        return {"flair_sentiment":sign*total_sentiment[0].score}
    
    def get_flair_fast(self, text):
            
        if len(text) == 0:
            return {"flair_fast_sentiment": -1}
        s = Sentence(text)
        self.flair_fast.predict(s)
        total_sentiment = s.labels

        sign = -2*(total_sentiment[0].value=="NEGATIVE")+1.0
        
        return {"flair_fast_sentiment":sign*total_sentiment[0].score}
    
    def get_textblob(self, text):
        polarity = TextBlob(text).sentiment.polarity
        return {"polarity":polarity}
    
    def get_vader(self, text):
        result = self.sid.polarity_scores(text)
        return {"polarity_positive":result.get('pos'),
                "polarity_negative":result.get('neg'),
                "polarity_compound":result.get('compound')}
        