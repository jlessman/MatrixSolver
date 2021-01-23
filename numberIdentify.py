#!pip install tensorflow keras numpy mnist matplotlib

import numpy as np
import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential #Neural stuff
from keras.layers import Dense
from keras.utils import to_categorical

def numberAnalyzer(numberData):
    # re-establishing model
    model = Sequential()
    model.add( Dense(64, activation='relu', input_dim=784))
    model.add( Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(
        optimizer='adam',
        loss = 'categorical_crossentropy',
        metrics = ['accuracy']
        )
    model.load_weights('model.h5')

    # transforming image
    numberData = (numberData/255) - 0.5
    numberData = numberData.reshape(-1,784)
    
    # caluclations
    number = np.argmax(model.predict(numberData), axis = 1)
    
    return number

    