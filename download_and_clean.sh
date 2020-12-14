#gcloud auth login
mkdir raw_tweet_data

gsutil -m cp -r gs://trends_dynamics/Tweet_Data_New/* raw_tweet_data/
gsutil -m cp -r gs://trends_dynamics/More_Tweet_Data/* raw_tweet_data/
#mv Tweet_Data_New tweet_data
python clean_data.py
