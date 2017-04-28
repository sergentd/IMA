#!/usr/bin/env python3
"""
This script permit to convert videos into matrix which all of same size
of Openface's Action Units (AU).
"""
import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def parse():
    parser = argparse.ArgumentParser(description="""
        Convert videos into matrix which all of same size
        of Openface's Action Units.
        """)
    parser.add_argument(
        '-s', '-source',
        metavar='DIR/VID',
        type=dir,
        default="../data/vid_usr",
        help='file where you generate your videos with showVid.ipynb')
    parser.add_argument(
        '-t', '-target',
        metavar='DIR/VID',
        type=dir,
        default="../data/vid_usr",
        help='file where you generate your videos with showVid.ipynb')
    return parser

def __get_data__():
    pass


def main():
    parser = parse()



if __name__ == '__main__':
    main()
