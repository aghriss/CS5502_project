########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     main.py
# Purpose:  Run different python packages to normalize, train,
#           test, and evaluate NLP model
########################################################################

############################
# Imports
############################
import tensorflow as tf
import configparser
import pickle


from Normalizing.ReadFile import ReadFile
from Normalizing.Normalize import Normalize
from Normalizing.Split import Split

from Fitting.LogReg import LogRegModel
from Fitting.DNN import DnnModel
from Fitting.RanFor import RanForModel

from Predicting.LogReg import LogRegPred
from Predicting.DNN import DnnPred
from Predicting.RanFor import RanForPred

from Evaluating.EvalModel import EvalModel


############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('./_config.ini')

rawDataFile = config["RawData"]["FileName"]
normSplitFile = config["NormData"]["Split"]
normNotSplitFile = config["NormData"]["NotSplit"]

trainPercent = float(config["Eval"]["trainPercent"])

logRegModelFile = config["Model"]["LogReg"]
dnnModelFile = config["Model"]["Dnn"]
ranForModelFile = config["Model"]["RanFor"]

logRegPredFile = config["Pred"]["LogReg"]
dnnPredFile = config["Pred"]["Dnn"]
ranForPredFile = config["Pred"]["RanFor"]


def DumpPickle(fileName, data):
    with open(fileName, "wb") as handle:
        pickle.dump(data, handle)

def RawDataToNormData():
    rf = ReadFile(rawDataFile)
    norm = Normalize(rf.df)
    split = Split(norm.df, trainPercent)
    DumpPickle(normNotSplitFile, [split.xTotal, split.yTotal])
    DumpPickle(normSplitFile, [split.xTrain, split.yTrain, split.xTest, split.yTest])

def ReadData(fileName):
    data = pickle.load(open(fileName,"rb"))
    xTrain = data[0]
    yTrain = data[1]

    xTest = data[2]
    yTest = data[3]
    return xTrain, yTrain, xTest, yTest





def FitLogRegModel():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    logReg = LogRegModel()
    logReg.setData(xTrain, yTrain)
    logReg.fit()
    DumpPickle(logRegModelFile, logReg.model)

def FitDnnModel():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    dnn = DnnModel()
    dnn.setData(xTrain, yTrain)
    dnn.fit()
    dnn.model.save(dnnModelFile)

def FitRanFor():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    ranFor = RanForModel()
    ranFor.setData(xTrain, yTrain)
    ranFor.fit()
    DumpPickle(ranForModelFile, ranFor.model)





def PredLogReg():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    logReg = pickle.load(open(logRegModelFile,"rb"))
    logRegPred = LogRegPred(logReg, xTest)
    DumpPickle(logRegPredFile, logRegPred.yPred)

def PredDnn():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    dnn = tf.keras.models.load_model(dnnModelFile)
    dnnPred = DnnPred(dnn, xTest)
    DumpPickle(dnnPredFile, dnnPred.yPred)

def PredRanFor():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    ranFor = pickle.load(open(ranForModelFile,"rb"))
    ranForPred = RanForPred(ranFor, xTest)
    DumpPickle(ranForPredFile, ranForPred.yPred)





def EvalLogReg():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    yPred = pickle.load(open(logRegPredFile,"rb"))
    evalModel = EvalModel(yPred, yTest)

def EvalDnn():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    yPred = pickle.load(open(dnnPredFile, "rb"))
    evalModel = EvalModel(yPred, yTest)

def EvalRanFor():
    xTrain, yTrain, xTest, yTest = ReadData(normSplitFile)
    yPred = pickle.load(open(ranForPredFile, "rb"))
    evalModel = EvalModel(yPred, yTest)



FitRanFor()
PredRanFor()
EvalRanFor()