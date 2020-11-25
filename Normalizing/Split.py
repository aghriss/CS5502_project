########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     Split.py
# Purpose:  Take in a dataframe
#           and split it into xTrain, yTrain, xTest, and yTest
########################################################################



class Split:
    def __init__(self, df, trainPercent):
        self.df = df
        self.trainPercent = trainPercent
        self.xTrain, self.yTrain, self.xTest, self.yTest, self.xTotal, self.yTotal = [], [], [], [], [], []
        self.split()

    def split(self):
        self.xTotal = self.df.drop(columns=['trending'])
        self.yTotal = self.df["trending"]
        cutOffTrain = (int)(self.trainPercent * len(self.xTotal))




        self.xTrain = self.xTotal[:cutOffTrain]
        self.yTrain = self.yTotal[:cutOffTrain]

        self.xTest = self.xTotal[cutOffTrain:]
        self.yTest = self.yTotal[cutOffTrain:]