########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     LogReg.py
# Purpose:  Predict a class when given a logistic regression model and
#           test data
########################################################################

############################
# Imports
############################

from sklearn.linear_model import LogisticRegression


############################
# Train Model
############################

class LogRegPred:
    def __init__(self, model, xTest):

        self.yPred = model.predict(xTest)