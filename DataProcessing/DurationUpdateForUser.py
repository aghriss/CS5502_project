#!/usr/bin/env python
# coding: utf-8

# In[136]:


import glob
import os
import pandas as pd
import datetime
from dateutil import relativedelta


# In[169]:


def calculateDuration(df):
    dates = df['userCreatedAt']
    format_str = '%Y-%m-%d %H:%M:%S'
    duration = []
    for date_str in dates:
        d0 = datetime.datetime.strptime(date_str, format_str)
        delta = relativedelta.relativedelta(datetime.datetime.now(), d0)
        full_months = (delta.years * 12) + delta.months
        duration.append(full_months)
    df['userOnTwitter(Months)'] = duration
    df.head()
    return df


# In[181]:


def readAndUpdateCSV():
    path = os.getcwd() + "\data_canada"
    all_files = glob.glob(path + "\*.csv")
    #2013-05-15 00:01:24
    for file in all_files:
        df = pd.read_csv(file)
        df.head()
        df = calculateDuration(df)
        df.to_csv(file)


# In[182]:


readAndUpdateCSV()


# In[ ]:





# In[ ]:




