#!/usr/bin/env python3
"""
This script permit to convert videos into matrix which
of Openface's Action Units (AU).
"""
import argparse
import os
from collections import defaultdict as dd
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np


def parse():
    """Parse."""
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
        default="../data/au_matrix/usr",
        help='dir where you want to store your AU matrix')
    parser.add_argument(
        '-r',
        metavar='DIR/AU_R',
        type=tuple,
        default=(True, "../data/au_matrix/resize"),
        help='Save a resize version of the output')
    return parser.parse_args()


def get_data_vid(source, target):
    """Walk files into data to convert each videos."""
    def useOpenface(save_point, vid_yt, ref_vid):
        command = "./../../OpenFace/build/bin/FeatureExtraction -f "
        command += vid_yt
        command += " -of "+ref_vid+".data -root "+save_point
        os.system(command)
    max_time = 0
    dict_matrix = dd(lambda: dd(list))
    for path_id_usr in os.listdir(source):
        for vid_yt in os.listdir(source+"/"+path_id_usr):
            if vid_yt[-3:] == "avi":
                ref_vid = vid_yt[:-4]
                if ref_vid+".data" not in os.listdir(source+"/"+path_id_usr):
                    useOpenface(source+"/"+path_id_usr, vid_yt, ref_vid)
                dataframe = pd.read_csv(
                    source+"/"+path_id_usr+"/"+ref_vid+".data")
                action_units = [dt for dt in dataframe.columns if dt[:3]==" AU"]
                dataframe = dataframe[
                    dataframe.columns.intersection(action_units)]
                dict_matrix[path_id_usr][ref_vid] = dataframe
                os.system("mkdir "+target+"/"+path_id_usr)
                os.system("touch "+target+"/"+path_id_usr+"/"+ref_vid+".mt")
                with open(target+"/"+path_id_usr+"/"+ref_vid+".mt", "w") as myfile:
                    dataframe.to_csv(myfile)
                if dataframe.shape[0] > max_time:
                    max_time = dataframe.shape[0]
    return dict_matrix, max_time


def resize(dict_matrix, target, max_time):
    """Permit to do a resize of the matrix."""
    def interpolation(dataframe, max_time):

        old_matrix = dataframe.as_matrix()
        old_dim, n_col = old_matrix.shape[0], old_matrix.shape[1]
        new_dim = max_time
        new_matrix = np.zeros((max_time, n_col))
        nls, ols = np.linspace(0, 1, new_dim), np.linspace(0, 1, old_dim)
        for col in range(n_col):
            new_matrix[:, col] = np.interp(nls, ols, old_matrix[:, col])
        coll = list(dataframe)
        dataframe = pd.DataFrame(new_matrix, columns=coll)
        return dataframe

    # os.system("ls "+target)
    # print(dict_matrix, target, max_time)
    for path_id_usr in dict_matrix:
        for ref_vid in dict_matrix[path_id_usr]:
            dict_matrix[path_id_usr][ref_vid] = interpolation(
                dict_matrix[path_id_usr][ref_vid], max_time)
            dataframe = dict_matrix[path_id_usr][ref_vid]
            os.system("mkdir "+target+"/"+path_id_usr)
            os.system("touch "+target+"/"+path_id_usr+"/"+ref_vid+".mt")
            with open(target+"/"+path_id_usr+"/"+ref_vid+".mt", "w") as myfile:
                dataframe.to_csv(myfile)
    return dict_matrix


def main():
    """Do everything."""
    args = parse()
    source, target = args.s, args.t
    dm, max_time = get_data_vid(source, target)
    if args.r[0]:
        dm = resize(dm, args.r[1], max_time)
    return dm


if __name__ == '__main__':
    main()
