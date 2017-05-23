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
    pprint(funny_usr_vid)
    return grade_usr_vid, funny_usr_vid


def mt_to_vec(vec):
    pass


def _get_vectors():
    mt_usr_vid = dd(lambda: dd(pd.DataFrame))
    path = "../data/au_matrix/resize/"
    for usr in sorted(os.listdir(path)):
        for mt in sorted(os.listdir(path + usr)):
            with open(path + usr + "/" + mt) as stream:
                dataframe = pd.read_csv(stream)
            mt_usr_vid[usr][mt[:-3]] = dataframe
    pprint(mt_usr_vid["e01"]["02"])


def main():
    _get_vectors()


if __name__ == '__main__':
    main()
