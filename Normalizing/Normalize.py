########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     Normalize.py
# Purpose:  Take in a dataframe
#           and normalize all the data
########################################################################



class Normalize:
    def __init__(self, df):
        self.df = df
        self.df = self.normalizeData("min_max")

    def normalizeData(self, normType):
        for col in self.df.columns:
            self.df[col] = self.normalizeCol(self.df[col], normType)
        return self.df
    
    def normalizeCol(self, colData, type):
        mean = colData.mean()
        std = colData.std()
        maxVal = colData.max()
        minVal = colData.min()
        newMax = 1
        newMin = 0

        if type == "z_score":
            colData = (colData - mean) / std
        elif type == "min_max":
           colData = ((colData - minVal) * (newMax - newMin) / (maxVal - minVal)) + newMin

        return colData

