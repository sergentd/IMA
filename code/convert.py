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
    return parser.parse_args()


def get_data_vid(source):
    """ Walk files into data to convert each videos """
    def useOpenface(save_point, vid_yt , ref_vid):

        os.system("ls ../../../poggioe0/OpenFace/build/bin/FeatureExtraction")
        command = "./../../OpenFace/build/bin/FeatureExtraction -f "
        command += vid_yt
        command += " -of "+ref_vid+".txt -root "+save_point
        os.system(command)
    dict_matrix = dd(lambda: dd(list))
    for path_id_usr in os.listdir(source):
        for vid_yt in os.listdir(source+"/"+path_id_usr):
            ref_vid = vid_yt[:-4]
            useOpenface(source+"/"+path_id_usr, vid_yt, ref_vid)
            dict_matrix[path_id_usr][ref_vid] = [0, 0, 0, 0]


def resize():
    pass


def main():
    args = parse()
    source, target = args.s, args.t
    # print(source)
    get_data_vid(source)


if __name__ == '__main__':
    main()
