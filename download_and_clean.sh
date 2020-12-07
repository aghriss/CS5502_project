#gcloud auth login
gsutil -m cp -r gs://trends_dynamics/Tweet_Data_New .
mv Tweet_Data_New tweet_data
python clean_data.py
