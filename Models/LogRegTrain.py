
########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     LogRegTrain.py
# Purpose:  Read data from pickle file
#           train a model on the data
#           save the model
########################################################################

############################
# Imports
############################

import configparser
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression


############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('../_config.ini')

dataFile = config["NormData"]["FileName"]
outputFile = config["Model"]["LogReg"]


############################
# Read File
############################

df = pickle.load(open(dataFile,"rb"))

############################
# Split Data And Label
############################

data = df.drop(columns=['trending'])
labels = df["trending"]

############################
# Train Model
############################

log_reg = LogisticRegression(multi_class="ovr",solver="lbfgs", C=.1, max_iter=10000,n_jobs=-1)
log_reg.fit(data,labels)

############################
# Save Model
############################

with open(outputFile,"wb") as handle:
    pickle.dump(log_reg,handle)
