#!/usr/bin/env python
# coding: utf-8

# In[2]:


#packages
import pandas as pd
import os.path
import csv


# In[6]:


#Saving tweet data in csv
def saveTweetData(topicName, tweetId, createdAt, text, retweetCount, likeCount, isQuote, place, geo, hashtags, 
                  userMentions, source, sourceUrl, userId, userName, userScreenName, userCreatedAt, userFollowersCount, 
                  userDescription, userVerified,userProtected, userLocation, userFriendsCount, userStatusesCount, 
                  userListedCount, rawData):
    fileName = "data/"+topicName+".csv"
    if (os.path.isfile(fileName)):
        #print("filename", fileName, "again")
        with open(fileName, 'a', encoding='UTF-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["", tweetId, createdAt, text, retweetCount, likeCount, isQuote, place, geo, hashtags, 
                  userMentions, source, sourceUrl, userId, userName, userScreenName, userCreatedAt, userFollowersCount, 
                  userDescription, userVerified,userProtected, userLocation, userFriendsCount, userStatusesCount, 
                  userListedCount, rawData])
    else :
        tweetDict = {'tweetId':tweetId, 'createdAt':createdAt, 'text':text, 'retweetCount':retweetCount, 'likeCount':likeCount, 'isQuote':isQuote, 
                  'place':place, 'geo':geo, 'hashtags':hashtags, 'userMentions':userMentions, 'source':source,'sourceUrl':sourceUrl, 
                 'userId':userId, 'userName':userName, 'userScreenName':userScreenName, 'userCreatedAt':userCreatedAt, 'userFollowersCount':userFollowersCount, 
                 'userDescription':userDescription, 'userVerified':userVerified,'userProtected':userProtected, 'userLocation':userLocation, 
                 'userFriendsCount':userFriendsCount, 'userStatusesCount':userStatusesCount, 'userListedCount':userListedCount, 'rawData':rawData}
        tweetDf = pd.DataFrame(tweetDict, index=[0])
        tweetDf.to_csv(fileName)


# In[ ]:




