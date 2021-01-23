!pip install tensorflow keras numpy mnist matplotlib

import numpy as np
import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential #Neural stuff
from keras.layers import Dense
from keras.utils import to_categorical


train_images = mnist.train_images() #data images
train_labels = mnist.train_labels() #data labels
test_images = mnist.test_images() #training test
test_labels = mnist.test_labels() #training labels

#normalizing array
train_images = (train_images/255) - .5
test_images = (test_images/255) - .5

#flat em into vector
train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))

#model building
model = Sequential()
model.add( Dense(64, activation='relu', input_dim=784))
model.add( Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

#compile the model
#loss function (how well training did + improvement)
model.compile(
    optimizer='adam',
     loss = 'categorical_crossentropy',
     metrics = ['accuracy']
)

#train the model
model.fit(
    train_images,
     to_categorical(train_labels),
     epochs = 5,
     batch_size = 32
)

model.evaluate(
    test_images,
     to_categorical(test_labels)
)

model.save_weights(filepath='model.h5')