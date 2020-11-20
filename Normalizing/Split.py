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
        self.xTrain, self.yTrain, self.xTest, self.yTest = [], [], [], []
        self.split()

    def split(self):
        data = self.df.drop(columns=['trending'])
        labels = self.df["trending"]
        cutOffTrain = (int)(self.trainPercent * len(data))


        self.xTrain = data[:cutOffTrain]
        self.yTrain = labels[:cutOffTrain]

        self.xTest = data[cutOffTrain:]
        self.yTest = labels[cutOffTrain:]