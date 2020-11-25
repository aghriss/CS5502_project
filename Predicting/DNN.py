########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     DNN.py
# Purpose:  Predict a class when given a DNN model and
#           test data
########################################################################

############################
# Imports
############################

import tensorflow as tf


############################
# Train Model
############################

class DnnPred:
    def __init__(self, model, xTest):
        self.yPred = model.predict_classes(xTest)