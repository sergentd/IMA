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


def parse():
    parser = argparse.ArgumentParser(description="""
        Convert videos into matrix which
        of Openface's Action Units.
        """)
    parser.add_argument(
        '-s', '-source',
        metavar='DIR/VID',
        type=dir,
        default="../data/vid_usr",
        help='dir where you generate your videos with showVid.ipynb')
    parser.add_argument(
        '-t', '-target',
        metavar='DIR/AU',
        type=dir,
        default="../data/au_usr",
        help='dir where you want to store your AU matrix')
    return parser


def __get_data__(source):
    pass


def resize():
    pass


def main():
    args = parse()
    source, target = args.source, args.target
    __get_data__(source)
if __name__ == '__main__':
    main()
