########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     RanFor.py
# Purpose:  Predict a class when given a Random Forest model and
#           test data
########################################################################

############################
# Imports
############################

from sklearn.ensemble import RandomForestClassifier


############################
# Train Model
############################

class RanForPred:
    def __init__(self, model, xTest):

        self.yPred = model.predict(xTest)