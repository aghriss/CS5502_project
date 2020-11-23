########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     LogReg.py
# Purpose:  Train a logistic regression model on given data
########################################################################

############################
# Imports
############################

from sklearn.linear_model import LogisticRegression


############################
# Train Model
############################

class LogRegModel:

    def setData(self, xTrain,yTrain):
        self.xTrain = xTrain
        self.yTrain = yTrain
        self.model = LogisticRegression(multi_class="ovr",solver="lbfgs", C=.1, max_iter=10000,n_jobs=-1)

    def setParam(self, multiClass, solver, c, maxIter, nJobs):
        self.model = LogisticRegression(multi_class=multiClass,solver=solver, C=c, max_iter=maxIter,n_jobs=nJobs)

    def fit(self):
        self.model.fit(self.xTrain, self.yTrain)

