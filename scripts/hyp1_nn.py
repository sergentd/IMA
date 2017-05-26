#!/usr/bin/env python3
import utils.datasets as ds
import utils.mesure as ms
from keras.models import Sequential
from keras.layers import Dense, Activation
import keras


def main():
    str0 = ""
    all_usr_funny = []
    all_usr_grade = []

    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    del vid_usr, lusr
    hyp1 = ds.by_X(usr_vid)
    for usr in sorted(hyp1):
        list_uv = hyp1[usr]["keys"]

        vecs_test = ds.list_features(
            hyp1, [usr], "test", lvid, "vec")
        labels_test_funny = ds.list_features(
            hyp1, [usr], "test", lvid, "funny")
        labels_test_grade = ds.list_features(
            hyp1, [usr], "test", lvid, "grade")

        vecs_train = ds.list_features(
            hyp1, [usr], "train", list_uv, "vec")
        labels_train_funny = ds.list_features(
            hyp1, [usr], "train", list_uv, "funny")
        labels_train_grade = ds.list_features(
            hyp1, [usr], "train", list_uv, "grade")
        print(len(vecs_train[0]))
        model = Sequential()
        model.add(Dense(units=64, input_dim=len(vecs_train[0])))
        model.add(Activation('relu'))
        model.add(Dense(units=10))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy',
                      optimizer='sgd',
                      metrics=['accuracy'])
        model.compile(loss=keras.losses.categorical_crossentropy,
                      optimizer=keras.optimizers.SGD(
                          lr=0.01, momentum=0.9, nesterov=True))
        model.train_on_batch(vecs_train, labels_train_funny)

        classes = model.predict(vecs_test, batch_size=128)

        print(classes)

        break

    """
        str0 += "\n".join(["", usr, ms.all_mesure_funny(pred_funny),
                           ms.all_mesure_grade(pred_grade)])
        all_usr_funny.extend(pred_funny)
        all_usr_grade.extend(pred_grade)
    str0 += "\n".join(["", "all_usr", ms.all_mesure_funny(all_usr_funny),
                       ms.all_mesure_grade(all_usr_grade)])
    print(str0)"""


if __name__ == '__main__':
    main()
