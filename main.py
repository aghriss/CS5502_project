########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     main.py
# Purpose:  Run different python packages to normalize, train,
#           test, and evaluate NLP model
########################################################################



############################
# Imports
############################


from Normalizing.ReadFile import  ReadFile
from Normalizing.Normalize import Normalize
from Normalizing.Split import Split

from Models.LogRegTrain import LogReg
from Evaluation.EvalModel import EvalModel

from Models.DNN import DNN

import configparser
import pickle


############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('./_config.ini')

rawDataFile = config["RawData"]["FileName"]
normDataFile = config["NormData"]["FileName"]
trainPercent = float(config["Eval"]["trainPercent"])

logRegModelFile = config["Model"]["LogReg"]


def DumpPickle(fileName, data):
    with open(fileName, "wb") as handle:
        pickle.dump(data, handle)


def RawDataToNormData():
    rf = ReadFile(rawDataFile)
    norm = Normalize(rf.df)
    split = Split(norm.df, trainPercent)
    DumpPickle(normDataFile, [split.xTrain, split.yTrain, split.xTest, split.yTest])


def ReadData(fileName):
    data = pickle.load(open(fileName,"rb"))
    xTrain = data[0]
    yTrain = data[1]

    xTest = data[2]
    yTest = data[3]
    return xTrain, yTrain, xTest, yTest


def LogRegModel():
    xTrain, yTrain, xTest, yTest = ReadData(normDataFile)
    logReg = LogReg()
    logReg.setData(xTrain, yTrain)
    logReg.fit()
    DumpPickle(logRegModelFile, logReg.model)


def LogRegEval():
    xTrain, yTrain, xTest, yTest = ReadData(normDataFile)
    logReg = pickle.load(open(logRegModelFile,"rb"))
    evalModel = EvalModel(logReg, xTest, yTest)




xTrain, yTrain, xTest, yTest = ReadData(normDataFile)

dnn = DNN()
dnn.setData(xTrain, yTrain)
dnn.fit()