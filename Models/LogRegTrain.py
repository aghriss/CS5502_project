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

data = pickle.load(open(dataFile,"rb"))

xTrain = data[0]
yTrain = data[1]

xTest = data[2]
yTest = data[3]

############################
# Train Model
############################

class LogReg:
    def __init__(self, xTrain,yTrain):
        self.xTrain = xTrain
        self.yTrain = yTrain
        self.model = LogisticRegression(multi_class="ovr",solver="lbfgs", C=.1, max_iter=10000,n_jobs=-1)
        self.model.fit(xTrain, yTrain)

    def __init__(self, xTrain, yTrain, multiClass, solver, c, maxIter, nJobs):
        self.xTrain = xTrain
        self.yTrain = yTrain
        self.model = LogisticRegression(multi_class=multiClass,solver=solver, C=c, max_iter=maxIter,n_jobs=nJobs)
        self.model.fit(xTrain, yTrain)




############################
# Save Model
############################

with open(outputFile,"wb") as handle:
    pickle.dump(log_reg,handle)
