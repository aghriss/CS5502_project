########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     EvalModel.py
# Purpose:  Read model from pickle file
#           run the model on test data
#           save the result
########################################################################

############################
# Imports
############################

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score



class EvalModel:
    def __init__(self, model, xTest, yTest):

        yPred = model.predict(xTest)
        acc = accuracy_score(y_true = yTest, y_pred = yPred)
        prec = precision_score(y_true=yTest, y_pred=yPred)
        recall = recall_score(y_true=yTest, y_pred=yPred)

        print("Accuracy:\t" + str(acc))
        print("Precision:\t" + str(prec))
        print("Recall:\t" + str(recall))
