# CS5502_project
CS5502 Project

### Main File
* Most of the python files are part of packages in different folders
* main.py uses those file

### Pipeline
1. Normalizing
2. Fitting
3. Predicting
4. Evaluating

### Configuration Information
* _config.ini contains the filenames

### File Information

#### norm_all.p
* Contains all data
* [xTotal, yTotal]

#### norm_split.p
* Contains data in split format
* Split is done by the percent specified in _config.ini file
* trainPercent is the percent that will be used for training
* [xTrain, yTrain, xTest, yTest]

#### model_XXXXX.p
* Contains model that is fitted with the training data
* It could be a Scikit-Learn model or a TensorFlow model

#### pred_XXXXX.p
* Contains yPrediction when model is run through xTest
* While evaluating yPrediction will be compared with yTest to get metrics like accuracy and precision