#!/usr/bin/env python
# coding: utf-8

# In[110]:


#packages
import tweepy
import json


# In[111]:


# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)


# In[123]:


#initiate auth object
auth = tweepy.AppAuthHandler(creds['API_KEY'], creds['SECRET_KEY'])
api = tweepy.API(auth)

#Get tweet data by tweet_id 
tweet = api.get_status("967824267948773377", include_entities="true", include_ext_alt_text="true")
print(tweet)

print("\n")

# In[129]:


print("Tweet Attributes:")
print("tweet created at:",tweet.created_at)
print("tweet text:", tweet.text)
print("tweet text truncated:", tweet.truncated)
print("tweet retweet count:", tweet.retweet_count)
print("tweet fav. count:", tweet.favorite_count)
print("tweet is quote:", tweet.is_quote_status)
print("tweet source:", tweet.source)
print("Is tweet possibly sensitive:", tweet.possibly_sensitive)
print("tweet place:", tweet.place)
print("tweet geo:", tweet.geo)
print("tweet language:", tweet.lang)
print("Is this a retweet:", tweet.retweeted)
print("tweet contributors:", tweet.contributors)
print("tweet coordinates:", tweet.coordinates)
print("entities:", tweet.entities)
print("hastags:",tweet.entities['hashtags'])
print("users taged/ mentioned:", tweet.entities['user_mentions'])
print("url in tweet:", tweet.entities['urls'])
print("tweet source url", tweet.source_url)


# In[130]:


print("User Attributes:")
print("user name:",tweet.user.name)
print("user screen name:",tweet.user.screen_name)
print("user created at:", tweet.user.created_at)
print("user followers count:", tweet.user.followers_count)
print("user description:", tweet.user.description)
print("is user verified:", tweet.user.verified)
print("is user protected:", tweet.user.protected)
print("user location:", tweet.user.location)
print("user geo enabled:", tweet.user.geo_enabled)
print("user notification:", tweet.user.notifications)
print("user friends count:", tweet.user.friends_count)
print("user statuses count:", tweet.user.statuses_count)
print("user listed count:",tweet.user.listed_count)
print("user utc offset:", tweet.user.utc_offset)
print("user entities:", tweet.user.entities)


# In[131]:


#Get trends of particular place
#WOEID of USA
woied = 23424977

#Fetch trending tweets
trendArray = api.trends_place(woied)  #can add exclude = "hashtags" 

for trends in trendArray:
    for trendTopic in trends['trends']:
        print("Topic:", trendTopic['name'], "url:", trendTopic['url'], "tweet count:",trendTopic['tweet_volume'])


# In[ ]:




