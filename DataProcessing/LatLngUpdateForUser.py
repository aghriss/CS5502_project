#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import os
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time
import numpy as np


# In[2]:


def isNaN(str):
    return str != str


# In[7]:


def getLatLng(df):
    locator = Nominatim(user_agent="sgupadya@gmail.com")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    latLng = []
    for loc in df['userLocation']:
        #print(loc)
        if not isNaN(loc):
            location = geocode(loc)
            if location is None:
                latLng.append("200, 200") #Invlid lat lng
            else:
                latLng.append("{}, {}".format(location.latitude, location.longitude))
        else:
            latLng.append("200, 200") #Invlid lat lng
    df['userLatLng'] = latLng
    df.head()
    return df


# In[15]:


def getLatLng2(df):
    locator = Nominatim(user_agent="sgupadya@gmail.com")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    latLng = []
    address = []
    for loc in df['userLocation']:
        if not isNaN(loc):
            address.append(loc)
        else:
            address.append("")
    df['address'] = address
    df['location'] = df['address'].apply(geocode)
    df['userLatLng'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    df = df.drop(columns=['address', 'location'])
    #print(df)
    return df


# In[20]:


def readAndUpdateLocCSV():
    path = os.getcwd() + "\data_india"
    all_files = glob.glob(path + "\*_popular.csv")
    #2013-05-15 00:01:24
    for file in all_files:
        df = pd.read_csv(file)
        df.head()
        df = getLatLng2(df)
        df.to_csv(file)


# In[21]:


readAndUpdateLocCSV()


# In[ ]:





# In[ ]:




