#!/usr/bin/env python3
"""
"""
# import argparse
import os
from collections import defaultdict as dd
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from copy import copy


def _get_labels():
    grade_usr_vid = dd(lambda: dd(int))
    funny_usr_vid = dd(lambda: dd(bool))
    path = "../data/evals/"
    for usr_evals in sorted(os.listdir(path)):
        with open(path + usr_evals) as stream:
            dataframe = pd.read_csv(stream)
        for line in dataframe.values:
            grade_usr_vid[line[0]][line[1][:-4]] = line[2]
            funny_usr_vid[line[0]][line[1][:-4]] = line[3]
    # pprint(funny_usr_vid)
    return grade_usr_vid, funny_usr_vid


def mt_to_vec(mt):
    return [j for i in mt for j in i]


def _get_matrix():
    mt_usr_vid = dd(lambda: dd(pd.DataFrame))
    path = "../data/au_matrix/resize/"
    for usr in sorted(os.listdir(path)):
        for mt in sorted(os.listdir(path + usr)):
            with open(path + usr + "/" + mt) as stream:
                dataframe = pd.read_csv(stream)
            mt_usr_vid[usr][mt[:-3]] = dataframe
    return mt_usr_vid


def combine_datas():
    lusr, lvid = set(), set()
    all_usr_vid = dd(lambda: dd(dict))
    all_vid_usr = dd(lambda: dd(dict))
    mt_usr_vid = _get_matrix()
    grade_usr_vid, funny_usr_vid = _get_labels()
    for usr in sorted(mt_usr_vid):
        for vid in sorted(mt_usr_vid[usr]):
            created = {
                "funny": funny_usr_vid[usr][vid],
                "grade": grade_usr_vid[usr][vid],
                # "matrix": mt_usr_vid[usr][vid],
                "vec": np.array(mt_to_vec(mt_usr_vid[usr][vid].as_matrix()))
            }
            all_usr_vid[usr][vid] = created
            all_vid_usr[vid][usr] = created
            lusr.add(usr)
            lvid.add(vid)
    return all_usr_vid, all_vid_usr, sorted(list(lusr)), sorted(list(lvid))


def by_X(combine):
    one_X_test = dd(dict)
    for X in combine:
        copy_combine = copy(combine)
        copy_combine.pop(X)
        one_X_test[X] = {
            "test": combine[X],
            "train": copy_combine
        }
    return one_X_test


def usr_specific(combine, lvid, nbvid_test):
    all_usr_specific_vid = dd(lambda: dd(lambda: dd(dict)))
    lvid_test, lvid_train = lvid[:nbvid_test], lvid[nbvid_test:]
    for usr in combine:
        for vid in lvid_test:
            all_usr_specific_vid[usr]['test'][vid] = combine[usr][vid]
        for vid in lvid_train:
            all_usr_specific_vid[usr]['train'][vid] = combine[usr][vid]
    return all_usr_specific_vid


def list_features(thisdict, lvou1, trainortest, lvou2, value):
    list_feat = []
    for vou1 in sorted(lvou1):
        for vou2 in sorted(lvou2):
            if vou2 in thisdict[vou1][trainortest]:
                list_feat.append(thisdict[vou1][trainortest][vou2][value])
    return list_feat


def yolo():
    print("yolo")


def main():
    usr_vid, vid_usr, lusr, lvid = combine_datas()
    by_usr = by_X(usr_vid)
    a = usr_specific(usr_vid, lvid, 10)
    b = list_features(a, ["e02"], "test", lvid, "vec")
    pprint(b)
    # by_vid = by_X(vid_usr)
    # print(sorted(by_usr["e02"]["train"].keys()))
    # print(len(by_usr["e02"]["test"]["02"]["vec"]))
    # print()
    # print(sorted(by_vid["02"]["train"].keys()))
    # print(len(by_vid["03"]["test"]["e02"]["vec"]))
    # a = usr_specific(usr_vid, lvid, 10)
    # print(a["e02"]["test"]["07"])
    # print(len(a["e02"]["train"].keys()))


if __name__ == '__main__':
    main()
