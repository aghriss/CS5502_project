########################################################################
# Project:  CSCI 5502 Data Mining Project
# Name:     DNN.py
# Purpose:  Read data from pickle file
#           train a model on the data
#           save the model
########################################################################

############################
# Imports
############################

import configparser
import pickle
import numpy as np

import tensorflow as tf

############################
# Configuration Information
############################
config = configparser.ConfigParser()
config.read('../_config.ini')

dataFile = config["NormData"]["FileName"]
outputFile = config["Model"]["LogReg"]

NUM_LABELS = 7
BATCH_SIZE = 500
EPOCHS = 20
STEPS_PER_EPOCH = 100
NUM_FEATURES = 0

############################
# Read File
############################

data = pickle.load(open(dataFile,"rb"))

xTrain = data[0]
yTrain = data[1]

xTest = data[2]
yTest = data[3]


# creates batches from sparse X data(scipy csr_matrix format) and dense y data to hopefully save on memory
# if batch size is reasonably small, this should save memory quite a bit I think
def nn_batch_generator(X_data, y_data, batch_size):
    samples_per_epoch = X_data.shape[0]
    number_of_batches = samples_per_epoch / batch_size
    counter = 0

    index = np.arange(y_data.shape[0])

    while 1:
        index_batch = index[batch_size * counter:batch_size * (counter + 1)]
        X_batch = X_data[index_batch, :].todense()
        y_batch = y_data[index_batch]
        y_batch = tf.keras.utils.to_categorical(y_batch)
        counter += 1
        yield np.array(X_batch), y_batch
        if (counter > number_of_batches):
            counter = 0





############################
# Train Model
############################
NUM_FEATURES = xTrain.shape[0]
nn_clf = tf.compat.v2.keras.Sequential([
    tf.keras.layers.Dense(700, input_dim=NUM_FEATURES, activation="relu"),
    tf.keras.layers.Dense(500, activation="relu"),
    tf.keras.layers.Dense(300, activation="relu"),
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(20, activation="relu"),
    tf.keras.layers.Dense(NUM_LABELS, activation="softmax")
])

# Can also use sparse_categorical_accuracy as a metric
nn_clf.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=1e-3), loss='categorical_crossentropy',
               metrics=["accuracy", tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])

nn_clf_history = nn_clf.fit_generator(nn_batch_generator(xTrain, yTrain, BATCH_SIZE), epochs=EPOCHS,
                                      steps_per_epoch=STEPS_PER_EPOCH, shuffle="batch")



