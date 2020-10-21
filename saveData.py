#!/usr/bin/env python
# coding: utf-8

# In[1]:


#packages
import pandas as pd


# In[1]:


#Saving tweet data in csv
#TODO:need to change the function args
def saveTweetData(tweetIds, userIds, retweets, likes, replies, shares, isPinned, quotes, text, hashtags, hashLinks, hasMedia, dateTime, location, deviceInfo, isThread, threads):
    #tweet attributes dict
    tweetDict = {'tweetId':tweetIds, 'userId':userIds, 'retweet':retweets, 'likes':likes, 'replies':replies, 'shares':shares, 'isPinned':isPinned, 'quotes':quotes, 'text':text, 'hashtags':hashtags, 'hasLinks':hashLinks, 'hasMedia':hasMedia, 'dateTime':dateTime, 'location':location, 'deviceInfo':deviceInfo, 'isThread':isThread, 'threads':threads}
    
    tweetDf = pd.DataFrame(tweetDict)
    
    tweetDf.to_csv('tweet_data.csv')


# In[2]:


#Saving user data in csv
#TODO:need to change the function args
def saveUserData(userIds, names, frequency, followers, following, isVerfied, creationDates, tweets, location):
    #user attributes dict
    userDict = {'userId':userIds, 'name':names,'frequency':frequency, 'followers':followers, 'following':following, 'isVerified':isVerfied, 'creationDate':creationDates, 'tweets':tweets, 'location':location}
    
    userDF = pd.DataFrame(userDict)
    
    userDF.to_csv('user_data.csv')


# In[ ]:




