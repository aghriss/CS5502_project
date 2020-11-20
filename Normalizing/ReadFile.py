########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     ReadFile.py
# Purpose:  Read data from CSV file and turn the data into
#           a dataframe format
########################################################################


import pandas as pd


class ReadFile:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName)
        self.df = self.df.drop(columns=['Unnamed: 0'])