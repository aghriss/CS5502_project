import SentimentAnalysis as NLP
import pandas as pd
import os
import datetime
from dateutil import relativedelta
from DataProcessing.bigram_features import extract_bigrams_from_corpus
from DataProcessing.bigram_features import extract_bigrams_from_text, getUniqFeat
import re
import numpy as np
import argparse

    
def date_to_months(date_str):
    format_str = '%Y-%m-%d %H:%M:%S'
    d0 = datetime.datetime.strptime(date_str, format_str)
    delta = relativedelta.relativedelta(datetime.datetime.now(), d0)
    full_months = (delta.years * 12) + delta.months
    return full_months

def tweet_source(source):
    source = str(source)
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

def remove_retweet(text):
    return re.sub('^RT.*? : ', '', text,1)

def clean_text(df):
    df['text'] = df['text'].map(NLP.cleanup)
    df['text'] = df['text'].map(remove_retweet)
    return df

def bigram_feats(text, bigrams_corpus):
    bigrams = extract_bigrams_from_text(text)
    feats = getUniqFeat(bigrams, bigrams_corpus, 5)
    return {"feat_%i"%i:v/len(bigrams_corpus) for i,v in enumerate(feats)}


def assemble_sentences(folder):
    files = os.listdir(folder)
    sentences = []
    for i,f in enumerate(files):
        try:
            df= pd.read_csv(os.path.join(folder, f),index_col=0,encoding='utf-8')
            sentences += list(clean_text(df)['text'])
        except:
            print("Error reading %s"%f)
    return "\n".join(sentences)
                    

def transform_data(data_location, target_location):
    nlp_features = NLP.NLP_features()
    files = os.listdir(data_location)
    corpus = assemble_sentences(data_location)
    bigrams_corpus = extract_bigrams_from_corpus(corpus)
    df_combined = pd.DataFrame()
    
    for i,f in enumerate(files):
        trending = 0
        
        if f.split(".")[0].split("_")[-1]=='popular':
            trending = 1
        try:
            df = pd.read_csv(os.path.join(data_location, f),index_col=0,encoding='utf-8')
        except:
            print("Error reading file %s"%f)
            continue
        # add trending label
        print("Tranforming file %s"%f)
        df['trending'] = trending
        
        df = clean_text(df)
        
        # add bigrams features
        df = pd.concat([df,
                df['text'].apply(lambda x: pd.Series(bigram_feats(x,bigrams_corpus)))],
                       axis=1, join='inner')
        # add sentiment features
        
        df = pd.concat([df, df['text'].apply(lambda x: pd.Series(nlp_features.get_features(x)))],
               axis=1, join='inner')
        
        df['userCreatedAt'] = df['userCreatedAt'].map(date_to_months)
        df["source"] = df["source"].map(tweet_source)
        if 'userLatLng' not in df.columns:
            df['userLatLng'] = np.nan
        
        df['userLatLng'].fillna("(0,0,0)",inplace=True)
        df['latitude'] = df['userLatLng'].apply(user_lat)
        df['longitude'] = df['userLatLng'].apply(user_lng)
        
        df = df[['text', 'retweetCount', 'likeCount', 'isQuote',
                 'source', 'userId', 'userFollowersCount',
                 'userVerified', 'userProtected', 'userFriendsCount',
                 'userStatusesCount', 'userListedCount',
                 'userOnTwitter(Months)', 'trending',
                 'feat_0', 'feat_1', 'feat_2', 'feat_3', 'feat_4', 
                 #'latitude','longitude',
                 'flair_sentiment', 'flair_fast_sentiment', 'polarity',
                 'polarity_positive', 'polarity_negative', 'polarity_compound']]
        
        df_combined = pd.concat([df_combined, df],axis=0)
    
    print("Saving merge.csv to %s"%target_location)
    df_combined.to_csv(os.path.join(target_location, "merged_data.csv"),encoding = "utf-8")
            

def merge_data(target_location):
    files = os.listdir(target_location)
    df = pd.DataFrame()
    for i,f in enumerate(files):
        print("Merging %i/%i, %s"%(i+1,len(files),f))
        df2 = pd.read_csv(os.path.join(target_location, f),index_col=0,encoding='utf-8')
        df = pd.concat([df,df2],axis=0)
    df.to_csv(os.path.join(target_location, "merged_data.csv"),encoding = "utf-8")
    
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Tranform data and merge it')
    parser.add_argument('--data_location', type=str,help='where data is located')
    parser.add_argument('--target_location', type=str,help='where meregd data will be saved')
    args = parser.parse_args()
    data_location = args.data_location
    target_location = args.target_location
    try:
        os.mkdir(target_location)
    except:
        print("Folder %s already exists"%target_location)
    transform_data(data_location, target_location)

    
    