########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     ReadFile.py
# Purpose:  Read data from CSV file and turn the data into
#           a format that can be fed into the model.
#           Save the newly formatted data into a pickle file
########################################################################

############################
# Imports
############################

import pandas as pd
import numpy as np
import pickle

############################
# Configuration Information
############################


dataFile = "../Data/sample.csv"


############################
# Read File
############################

df = pd.read_csv(dataFile)
print(df)


############################
# Normalize
############################

############################
# Save As Pickle File
############################
