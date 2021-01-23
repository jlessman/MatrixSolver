#!pip install tensorflow keras numpy emnist matplotlib

import numpy as np
import emnist
import matplotlib.pyplot as plt
from keras.models import Sequential #Neural stuff
from keras.layers import Dense
from keras.utils import to_categorical

images, labels = emnist.extract_training_samples('digits')
images = (images/255)
images = images.reshape((-1,784))

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
    images,
     to_categorical(labels),
     epochs = 5,
     batch_size = 32
)

images, labels = emnist.extract_training_samples('mnist')
images = (images/255)
images = images.reshape((-1,784))

model.fit(
    images,
     to_categorical(labels),
     epochs = 5,
     batch_size = 32
)

images, labels = emnist.extract_test_samples('mnist')
images = (images/255)
images = images.reshape((-1,784))

model.evaluate(
    images,
     to_categorical(labels)
)

model.save_weights(filepath='model.h5')