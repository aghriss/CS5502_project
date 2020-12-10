import tweepy
import json
#import importlib
#import saveData
#from saveData import saveTweetData
import os
#with open("twitter_credentials.json", "r") as file:
#    creds = json.load(file)
#auth = tweepy.AppAuthHandler(creds['API_KEY'], creds['SECRET_KEY'])
#api = tweepy.API(auth)
import time


def get_counts_quantile(tweets):
    counts = []
    for t in tweets:
        counts.append()

def save_tweet(result):
    """Function to save tweepy result status"""
    pass
def save_user(result_set):
    """Function to save tweepy set fo result statuses"""
    pass

class TweetCrawler():
    
    def __init__(self, credentials_path, save_path, location_id=None):
        
        assert os.path.exists(save_path)
        assert os.path.exists(credentials_path)
        self.save_path = save_path
        self.location_id = 23424977
        try:
            with open(credentials_path,"r") as f:
                creds = json.load(f)
                f.close()
            self.api = tweepy.API(tweepy.AppAuthHandler(creds['API_KEY'], creds['SECRET_KEY']))
        except:
            raise "Auth Error, check credentials and connection"
        if location_id:
            self.location_id = location_id
        
    def crawl(self):
        location, trends = self.get_trends()
        for trend in trends:
            query = trend['query']
            trending = self.get_trending_tweets(query)
            non_trending = self.get_untrending_tweets(query)
        
        self.store(trending, trending=True)
        self.store(non_trending, trensing=False)
            
                
    def get_trends(self,):
        
        trends_dict = self.api.trends_place(self.location_id)[0]
        
        location_name = trends_dict['locations'][0]['name']
        non_empty_trends = list(filter(lambda x: x['tweet_volume'] is not None,
                                       trends_dict['trends']))
        print("Retrieved %i for location: %s"%(len(non_empty_trends), location_name))
        return location_name, non_empty_trends
    
    
    def get_trending_tweets(self, query):
        popular_tweets = self.api.search(query, count=500, result_type="popular")
        tuples = []
        for popular in popular_tweets:
            user_timeline = self.api.user_timeline(popular.author.id, count=200)
            tuples.append([popular, user_timeline])
        return tuples
    
    def get_untrending_tweets(self, query):
        popular_tweets = self.api.search(query, count=500, result_type="recent")
        tuples = []
        for popular in popular_tweets:
            user_timeline = self.get_user(popular.author.id)
            tuples.append([popular, user_timeline])
        return tuples

    def get_user(self, user_id):
        time.sleep(0.1)
        return self.api.user_timeline(user_id, count=200)

    def save_user(self, user):
        print("Saving user %s"%user.id_str)
        json.dump(user._json, open(os.path.join(self.save_path, "user_"+user.id_str+".json"), 'w'))
        
    def save_tweet(self, tweet):
        print("Saving tweet %s"%tweet.id_str)
        json.dump(tweet._json, open(os.path.join(self.save_path, "tweet_"+ tweet.id_str+".json"), 'w'))
    
    def rate_status(self):
        state =  self.api.rate_limit_status()
        limits = state['resources']['statuses']
        return {'tweet':limits['/statuses/show/:id']['remaining'],
                'users': limits['/statuses/user_timeline']['remaining']}
    def get_tweet(self, tweet_id):
        time.sleep(0.1)
        return self.api.get_status(tweet_id)
        
        

#crawler = TweetCrawler("twitter_credentials.json", './data')
#self=crawler

