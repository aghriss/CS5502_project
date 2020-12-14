'''
Code used to update tweets
'''

import pandas as pd
import os

from TwitterCode.crawler import TweetCrawler
from tweepy import TweepError
import time

def read_labels(data_location, target_location):


    crawler = TweetCrawler("./TwitterCode/twitter_credentials.json", "cleaned_tweet_data")
    user_ids = []
    files = os.listdir(data_location)    
    errors = []
    crawled = os.listdir("cleaned_tweet_data")
    for i,f in enumerate(files):
        trending = 0
        
        if f.split(".")[0].split("_")[-1]=='popular':
            trending = 1
        try:
            df = pd.read_csv(os.path.join(data_location, f),index_col=0,encoding='utf-8')
        except:
            print("Error reading file %s"%f)
            continue

        ids = list(df.tweetId)
        for iD in ids:
            
            while True:
                try:
                    print(crawler.rate_status())
                    time.sleep(0.1)
                    break
                except:
                    print("Rate limit exceeded, wait 10s")
                    time.sleep(10)
            
            if ("tweet_"+str(iD)+'.json') in crawled:
                continue
            print("Updating tweet", iD)
            try:
                tweet = crawler.get_tweet(iD)
                tweet._json['trending'] = trending
                crawler.save_tweet(tweet)
                crawler.save_user(tweet.user)
                
                if trending and tweet.user.id not in user_ids:
                    
                    timeline = crawler.get_user(tweet.user.id)
                    for tw in timeline:
                        tw._json["from_trending"] = trending
                        crawler.save_tweet(tw)
                    user_ids.append(tweet.user.id)
                    
                    
            except TweepError as e:
                    #e = sys.exc_info()[0]
                errors.append([iD, e])
                print(i, e)
                
                
read_labels("./tweet_data","")
