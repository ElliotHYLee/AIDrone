from keras.models import Sequential
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.layers import Activation, Dense


def getModel(input_dim):
    model = Sequential()
    model.add(Dense(input_dim, input_dim=input_dim, kernel_initializer="uniform", activation=LeakyReLU()))
    model.add(Dense(20, kernel_initializer="uniform", activation=LeakyReLU()))
    model.add(Dense(10, kernel_initializer="uniform", activation=LeakyReLU()))
    #model.add(Dense(5, kernel_initializer="uniform", activation=LeakyReLU()))
    model.add(Dense(2, kernel_initializer="uniform", activation='linear'))
    model.compile(loss='mse', optimizer='adam')
    return model
