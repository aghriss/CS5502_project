########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     DNN.py
# Purpose:  Train DNN model on given training data
########################################################################

############################
# Imports
############################

import tensorflow as tf


############################
# Train Model
############################

class DnnModel:

    def setData(self, xTrain,yTrain):
        self.xTrain = xTrain
        self.yTrain = yTrain

        self.trainTensor = tf.data.Dataset.from_tensor_slices((xTrain.values, yTrain.values))
        self.trainBatch = self.trainTensor.shuffle(len(xTrain)).batch(1)

        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(20, input_dim=xTrain.shape[1], activation="relu"),
            tf.keras.layers.Dense(12, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid")
        ])

        self.model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])



    def fit(self):
        self.nnClfHistory = self.model.fit(self.trainBatch, epochs=150)



