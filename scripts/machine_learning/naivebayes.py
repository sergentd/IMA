#!/usr/bin/env python3
"""
"""
# import argparse
import os
from sklearn.naive_bayes import GaussianNB
from collections import defaultdict as dd
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import utils.datasets as ds
from pprint import pprint


def create_nb_model(vecs_train, labels_train):
    return GaussianNB().fit(vecs_train, labels_train)


def nb_predict(nb_model, vecs_test, labels_test):
    return [(nb_model.predict([x])[0], y) for x, y in zip(
        vecs_test, labels_test)]


def main():
    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    del vid_usr
    test_system = ds.usr_specific(usr_vid, lvid, 10)
    for tested_usr in lusr:
        print(tested_usr)
        vecs_test = ds.list_features(
            test_system, [tested_usr], "test", lvid, "vec")
        labels_test = ds.list_features(
            test_system, [tested_usr], "test", lvid, "grade")
        vecs_train = ds.list_features(
            test_system, [tested_usr], "train", lvid, "vec")
        labels_train = ds.list_features(
            test_system, [tested_usr], "train", lvid, "grade")

        clf = GaussianNB()
        clf.fit(vecs_train, labels_train)

        total = 0
        ok = 0
        for x, y in zip(vecs_test, labels_test):
            if clf.predict([x])[0] == y:
                ok += 1
                total += 1
            else:
                total += 1
            print(clf.predict([x])[0], y)
        print(ok / total)
        print()


if __name__ == '__main__':
    main()
