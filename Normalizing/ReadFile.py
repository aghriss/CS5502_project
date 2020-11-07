########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     ReadFile.py
# Purpose:  Read data from CSV file and turn the data into
#           a format that can be fed into the model.
#           Save the newly formatted data into a pickle file
########################################################################

############################
# Imports
############################

import configparser
import pandas as pd
import numpy as np
import pickle


############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('../_config.ini')

dataFile = config["RawData"]["FileName"]
outputFile = config["NormData"]["FileName"]

trainPercent = float(config["Eval"]["trainPercent"])


############################
# Read File
############################

df = pd.read_csv(dataFile)

############################
# Cleaning
############################
# Get rid of unneeded columns
# Fix outliers
df = df.drop(columns=['Unnamed: 0'])

############################
# Normalize
############################

def normalizeData(df, normType):
    for col in df.columns:
        df[col] = normalizeCol(df[col], normType)
    return df

def normalizeCol(colData, type):
    mean = colData.mean()
    std = colData.std()
    maxVal = colData.max()
    minVal = colData.min()
    newMax = 1
    newMin = 0


    if type == "z_score":
        colData = (colData - mean) / std
    elif type == "min_max":
       colData = ((colData - minVal) * (newMax - newMin) / (maxVal - minVal)) + newMin

    return colData

df = normalizeData(df, "min_max")

############################
# Split the data
############################

data = df.drop(columns=['trending'])
labels = df["trending"]
cutOffTrain = (int)(trainPercent * len(data))


xTrain = data[:cutOffTrain]
yTrain = labels[:cutOffTrain]

xTest = data[cutOffTrain:]
yTest = labels[cutOffTrain:]


############################
# Save As Pickle File
############################

with open(outputFile, "wb") as handle:
    pickle.dump([xTrain, yTrain, xTest, yTest], handle)




