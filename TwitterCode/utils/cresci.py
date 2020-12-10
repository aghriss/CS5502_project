import pandas as pd
import io
import os

folder = "../datasets/cresci"

df_bot = pd.DataFrame()
df_gen = pd.DataFrame()
for f in os.listdir(folder):
    df = pd.read_csv(os.path.join(folder,f))
    if "spam" in f.lower() or "fake" in f.lower() or "bot" in f.lower():
        df_bot = pd.concat([df,df_bot])
    else:
        df_gen = pd.concat([df,df_gen])


bots = [ list(x) for x  in zip(list(df_bot['id']),len(df_bot)*['bot'])]
humans = [ list(x) for x in zip(list(df_gen['id']),len(df_gen)*['human'])]

al =[ x+["cresci-2017"] for x in bots+humans]
io.save_tsv("../tsv/creci2017.tsv",al)
