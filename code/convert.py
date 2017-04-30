#!/usr/bin/env python3
"""
This script permit to convert videos into matrix which
of Openface's Action Units (AU).
"""
import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict as dd


def parse():
    parser = argparse.ArgumentParser(description="""
        Convert videos into matrix which
        of Openface's Action Units.
        """)
    parser.add_argument(
        '-s',
        metavar='DIR/VID',
        type=str,
        default="../data/vid_usr",
        help='dir where you generate your videos with showVid.ipynb')
    parser.add_argument(
        '-t',
        metavar='DIR/AU',
        type=str,
        default="../data/au_matrix_usr",
        help='dir where you want to store your AU matrix')
    parser.add_argument(
        '-r',
        metavar='DIR/AU_R',
        type=tuple,
        default=(True, "../data/au_matrix_resize_usr"),
        help='Save a resize version of the output')
    return parser.parse_args()


def get_data_vid(source):
    """ Walk files into data to convert each videos """
    def useOpenface(save_point, vid_yt, ref_vid):
        command = "./../../OpenFace/build/bin/FeatureExtraction -f "
        command += vid_yt
        command += " -of "+ref_vid+".data -root "+save_point
        os.system(command)
    dict_matrix = dd(lambda: dd(list))
    for path_id_usr in os.listdir(source):
        for vid_yt in os.listdir(source+"/"+path_id_usr):
            if vid_yt[-3:] == "avi":
                ref_vid = vid_yt[:-4]
                if ref_vid+".data" not in os.listdir(source+"/"+path_id_usr):
                    useOpenface(source+"/"+path_id_usr, vid_yt, ref_vid)

                dict_matrix[path_id_usr][ref_vid] = [0, 0, 0, 0]
    return dict_matrix


def resize(dict_matrix, target):
    return dict_matrix


def main():
    args = parse()
    source, target = args.s, args.t
    dm = get_data_vid(source)
    if args.r[0]:
        resize(dm, args.r[1])


if __name__ == '__main__':
    main()
