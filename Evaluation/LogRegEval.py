########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     LogRegEval.py
# Purpose:  Read model from pickle file
#           run the model on test data
#           save the result
########################################################################

############################
# Imports
############################

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import configparser
import pandas as pd
import numpy as np
import pickle




############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('../_config.ini')

dataFile = config["NormData"]["FileName"]
modelFile = config["Model"]["LogReg"]

############################
# Read the model
############################

data = pickle.load(open(dataFile,"rb"))

xTrain = data[0]
yTrain = data[1]

xTest = data[2]
yTest = data[3]

log_reg = pickle.load(open(modelFile,"rb"))

############################
# Make predictions
############################
yPred = log_reg.predict(xTest)


############################
# Evaluate the predictions
############################

acc = accuracy_score(y_true = yTest, y_pred = yPred)
prec = precision_score(y_true=yTest, y_pred=yPred)
recall = recall_score(y_true=yTest, y_pred=yPred)

print("Accuracy:\t" + str(acc))
print("Precision:\t" + str(prec))
print("Recall:\t" + str(recall))
