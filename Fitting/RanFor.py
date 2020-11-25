########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     RanFor.py
# Purpose:  Train a random forest model on given data
########################################################################

############################
# Imports
############################

from sklearn.ensemble import RandomForestClassifier


############################
# Train Model
############################

class RanForModel:

    def setData(self, xTrain,yTrain):
        self.xTrain = xTrain
        self.yTrain = yTrain
        self.model = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=100)

    def setParam(self, nEstimators, nJobs, randomState):
        self.model = RandomForestClassifier(n_estimators=nEstimators, n_jobs=-nJobs, random_state=randomState)

    def fit(self):
        self.model.fit(self.xTrain, self.yTrain)

