#gcloud auth login
mkdir tweet_data

gsutil -m cp -r gs://trends_dynamics/Tweet_Data_New/* tweet_data/
gsutil -m cp -r gs://trends_dynamics/More_Tweet_Data/* tweet_data/
#mv Tweet_Data_New tweet_data
python clean_data.py
