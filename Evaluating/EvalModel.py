########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     EvalModel.py
# Purpose:  Evaluate given predictions and actual results
########################################################################

############################
# Imports
############################

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score



class EvalModel:


    def __init__(self, yPred, yTest):
        acc = accuracy_score(y_true = yTest, y_pred = yPred)
        prec = precision_score(y_true=yTest, y_pred=yPred)
        recall = recall_score(y_true=yTest, y_pred=yPred)

        print("Accuracy:\t" + str(acc))
        print("Precision:\t" + str(prec))
        print("Recall:\t" + str(recall))
