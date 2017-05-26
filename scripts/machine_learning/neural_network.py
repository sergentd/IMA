from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
import numpy as np
import tensorflow as tf


def create_trained_nn(vecs_train, labels_train):
    input_dim = vecs_train.shape[1]
    model = Sequential()
    model.add(Dense(units=100, input_dim=input_dim))
    model.add(Activation('relu'))
    model.add(Dense(units=20))
    model.add(Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    model.fit(vecs_train, labels_train, epochs=500, batch_size=32)
    return model


def convert_output(pred):
    return [bool(p) for p in pred]


def predict_nn(model, vecs_test, labels_test):
    return [(pred, label) for pred, label in zip(
        convert_output(model.predict_classes(vecs_test)), labels_test)]


def main():
    np.random.seed(3)
    vecs_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels_train = np.array([True, False, False, True])
    vecs_test = np.array([[0, 0], [1, 1], [1, 1]])
    labels_test = np.array([True, True, True])
    model = create_trained_nn(vecs_train, labels_train)

    print(predict_nn(model, vecs_test, labels_test))


if __name__ == '__main__':
    main()
