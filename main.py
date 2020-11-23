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

from Fitting.LogReg import LogRegModel
from Predicting.LogReg import LogRegPred

from Evaluating.EvalModel import EvalModel

from Fitting.DNN import DnnModel

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
dnnModelFile = config["Model"]["Dnn"]

logRegPredFile = config["Pred"]["LogReg"]
dnnPredFile = config["Pred"]["Dnn"]


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





def FitLogRegModel():
    xTrain, yTrain, xTest, yTest = ReadData(normDataFile)
    logReg = LogRegModel()
    logReg.setData(xTrain, yTrain)
    logReg.fit()
    DumpPickle(logRegModelFile, logReg.model)

def FitDnnModel():
    xTrain, yTrain, xTest, yTest = ReadData(normDataFile)
    dnn = DnnModel()
    dnn.setData(xTrain, yTrain)
    dnn.fit()
    DumpPickle(dnnModelFile, dnn.model)





def PredLogReg():
    xTrain, yTrain, xTest, yTest = ReadData(normDataFile)
    logReg = pickle.load(open(logRegModelFile,"rb"))
    logRegPred = LogRegPred(logReg, xTest)
    DumpPickle(logRegPredFile, logRegPred.yPred)

def PredDnn():
    pass





def EvalLogReg():
    xTrain, yTrain, xTest, yTest = ReadData(normDataFile)
    yPred = pickle.load(open(logRegPredFile,"rb"))
    evalModel = EvalModel(yPred, yTest)

def EvalDnn():
    pass



FitLogRegModel()
PredLogReg()
EvalLogReg()

