#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[68]:


def checkPopularTweetIDs(topicName):
    df = pd.read_csv("data_m/"+topicName+".csv")
    df_popular = pd.read_csv("data_m/"+topicName+"_popular.csv")
    tweetIds_popular = df_popular['tweetId'].values
    df['isPopular'] = np.where(df['tweetId'].isin(tweetIds_popular), 'Yes', 'No')
    print(len(df['tweetId'].values), len(df['isPopular'].values), len(df_popular['tweetId'].values))
    print(df['isPopular'].values)


# In[66]:


checkPopularTweetIDs("Thanksgiving")


# In[ ]:




