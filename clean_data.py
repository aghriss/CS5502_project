import SentimentAnalysis as NLP
import pandas as pd
import os
import datetime
from dateutil import relativedelta

folder = "./tweet_data"
dest_folder = "./cleaned_tweet_data"
try:
    os.mkdir(dest_folder)
except:
    print("Folder %s already exists"%dest_folder)
    
def date_to_months(date_str):
    format_str = '%Y-%m-%d %H:%M:%S'
    d0 = datetime.datetime.strptime(date_str, format_str)
    delta = relativedelta.relativedelta(datetime.datetime.now(), d0)
    full_months = (delta.years * 12) + delta.months
    return full_months
def tweet_source(source):
    if "WEB" in source.upper():
        return "WEB"
    if "ANDROID" in source.upper():
        return 'ANDROID'
    if "IPHONE" in source.upper():
        return "IPHONE"
    return "UNKNOWN"
def user_lat(location):
    return location.strip('(').split(",")[0]
def user_lng(location):
    return location.strip('(').split(",")[1]

def transform_data(folder, destination):
    nlp_features = NLP.NLP_features()
    files = os.listdir(folder)
    for i,f in enumerate(files):
        try:
            print("Tranformining %i/%i, %s"%(i+1,len(files),f))
            trending = 0
            if f.split(".")[0].split("_")[-1]=='popular':
                trending=1
            df = pd.read_csv(os.path.join(folder, f),index_col=0,encoding='iso-8859-1')
            df["trending"] = trending
    
            df['userCreatedAt'] = df['userCreatedAt'].map(date_to_months)
            df['text'] = df['text'].map(NLP.cleanup)
            df["source"] = df["source"].map(tweet_source)
            df['userLatLng'].fillna("(0,0,0)",inplace=True)
            df['latitude'] = df['userLatLng'].apply(user_lat)
            df['longitude'] = df['userLatLng'].apply(user_lng)
            df = pd.concat([df, df['text'].apply(lambda x: pd.Series(nlp_features.get_features(x)))],
                           axis=1, join='inner')
            df = df[['tweetId','text', 'retweetCount', 'likeCount', 'isQuote', 'source', 
                    'userId', 'userName','userScreenName', 'userCreatedAt', 'userFollowersCount',
                    'userVerified', 'userProtected', 'userFriendsCount', 'userStatusesCount',
                    'userListedCount', 'userOnTwitter(Months)', 'latitude', 'longitude',
                    'flair_sentiment', 'flair_fast_sentiment', 'polarity',
                    'polarity_positive', 'polarity_negative', 'polarity_compound', 'trending']]
            df.to_csv(os.path.join(dest_folder, f),encoding = "utf-8")
        except:
            print("Error processing file")

transform_data(folder, dest_folder)