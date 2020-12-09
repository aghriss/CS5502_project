import pandas as pd
import sys
import os

# python merge_csv.py folder

if __name__=="__main__":
    
    folder = sys.argv[1]
    print("Reading files from %s"%folder)
    df = pd.DataFrame()
    for f in os.listdir(folder):
        df = pd.concat([df,pd.read_csv(os.path.join(folder, f),index_col=0)],axis=0)
    df.to_csv("merged_data.csv")
        