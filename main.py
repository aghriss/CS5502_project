########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     main.py
# Purpose:  Run different python packages to normalize, train,
#           test, and evaluate NLP model
########################################################################



############################
# Imports
############################

# from Models.LogRegTrain import LogReg
from Normalizing.ReadFile import  ReadFile
from Normalizing.Normalize import Normalize
from Normalizing.Split import Split

import configparser
import pandas as pd
import numpy as np
import pickle


############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('./_config.ini')

rawDataFile = config["RawData"]["FileName"]
outputFile = config["NormData"]["FileName"]

trainPercent = float(config["Eval"]["trainPercent"])



def DumpPickle(fileName, data):
    with open(outputFile, "wb") as handle:
        pickle.dump(data, handle)



rf = ReadFile(rawDataFile)
norm = Normalize(rf.df)
split = Split(norm.df, trainPercent)
print(split.xTrain)
print(split.yTrain)
print(split.xTest)
print(split.yTest)



DumpPickle(outputFile, [split.xTrain, split.yTrain, split.xTest, split.yTest])
