#!/usr/bin/env python
# coding: utf-8

# In[38]:


#packages
import tweepy
import json
import importlib
import saveData
importlib.reload(saveData)
from saveData import saveTweetData


# In[24]:


# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)


# In[25]:


#initiate auth object
auth = tweepy.AppAuthHandler(creds['API_KEY'], creds['SECRET_KEY'])
api = tweepy.API(auth)


# In[26]:


#Get tweet data by tweet_id 
#tweet = api.get_status("967824267948773377", include_entities="true", include_ext_alt_text="true")
#print(tweet)


# In[47]:


# print("Tweet Attributes:")
# print("ID:",tweet.id)
# print("tweet created at:",tweet.created_at)
# print("tweet text:", tweet.text)
# print("tweet text truncated:", tweet.truncated)
# print("tweet retweet count:", tweet.retweet_count)
# print("tweet fav. count:", tweet.favorite_count)
# print("tweet is quote:", tweet.is_quote_status)
# print("tweet source:", tweet.source)
# print("Is tweet possibly sensitive:", tweet.possibly_sensitive)
# print("tweet place:", tweet.place)
# print("tweet geo:", tweet.geo)
# print("tweet language:", tweet.lang)
# print("Is this a retweet:", tweet.retweeted)
# print("tweet contributors:", tweet.contributors)
# print("tweet coordinates:", tweet.coordinates)
# print("entities:", tweet.entities)
# print("hastags:",tweet.entities['hashtags'])
# print("users taged/ mentioned:", tweet.entities['user_mentions'])
# print("url in tweet:", tweet.entities['urls'])
# print("tweet source url", tweet.source_url)


# In[ ]:


# print("User Attributes:")
# print("user name:",tweet.user.name)
# print("user screen name:",tweet.user.screen_name)
# print("user created at:", tweet.user.created_at)
# print("user followers count:", tweet.user.followers_count)
# print("user description:", tweet.user.description)
# print("is user verified:", tweet.user.verified)
# print("is user protected:", tweet.user.protected)
# print("user location:", tweet.user.location)
# print("user geo enabled:", tweet.user.geo_enabled)
# print("user notification:", tweet.user.notifications)
# print("user friends count:", tweet.user.friends_count)
# print("user statuses count:", tweet.user.statuses_count)
# print("user listed count:",tweet.user.listed_count)
# print("user utc offset:", tweet.user.utc_offset)
# print("user entities:", tweet.user.entities)


# In[44]:


#Get n tweets using queryText
def getTweetsFromTopic(query):
    trendTweets = api.search(query, count=500)
    count = 0
    for tweets in trendTweets:
        count+=1
        saveTweetData(query, tweets.id, tweets.created_at, tweets.text, tweets.retweet_count, tweets.favorite_count, tweets.is_quote_status, tweets.place, tweets.geo, ','.join(str(v) for v in tweets.entities['hashtags']), 
                  ','.join(str(v) for v in tweets.entities['user_mentions']), tweets.source, tweets.source_url, tweets.user.id, tweets.user.name, tweets.user.screen_name, tweets.user.created_at, tweets.user.followers_count, 
                  tweets.user.description, tweets.user.verified, tweets.user.protected, tweets.user.location, tweets.user.friends_count, tweets.user.statuses_count, 
                  tweets.user.listed_count)


# In[48]:


#Get n popular tweets using queryText
def getPopularTweetsFromTopic(query):
    trendTweets = api.search(query, count=500, result_type="popular")
    count = 0
    for tweets in trendTweets:
        count+=1
        saveTweetData(query+"_popular", tweets.id, tweets.created_at, tweets.text, tweets.retweet_count, tweets.favorite_count, tweets.is_quote_status, tweets.place, tweets.geo, ','.join(str(v) for v in tweets.entities['hashtags']), 
                  ','.join(str(v) for v in tweets.entities['user_mentions']), tweets.source, tweets.source_url, tweets.user.id, tweets.user.name, tweets.user.screen_name, tweets.user.created_at, tweets.user.followers_count, 
                  tweets.user.description, tweets.user.verified, tweets.user.protected, tweets.user.location, tweets.user.friends_count, tweets.user.statuses_count, 
                  tweets.user.listed_count)


# In[46]:


#Get trends of particular place
#WOEID of USA
woied = 23424977

#Fetch trending tweet topics and fetch respective tweets
trendArray = api.trends_place(woied)  #can add exclude = "hashtags" 
trendCount = 10
for trends in trendArray:
    for trendTopic in trends['trends']:
        if trendTopic['tweet_volume'] is None:
            continue
        #print("Topic:", trendTopic['name'], "url:", trendTopic['url'], "tweet count:",trendTopic['tweet_volume'], "query",trendTopic['query'])
        getTweetsFromTopic(trendTopic['query'])
        getPopularTweetsFromTopic(trendTopic['query'])
        trendCount-=1
        if trendCount == 0:
            break


# In[ ]:




