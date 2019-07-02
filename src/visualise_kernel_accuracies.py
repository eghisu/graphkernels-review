#!/usr/bin/env python3
#
# visualise_kernel_accuracies.py: visualises the individual kernels by
# means of their accuracies on the individual data sets. Multiple plot
# variants will be provided by this script (based on different metrics
# or dissimilarity measures).


import argparse

import pandas as pd
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT', type=str, help='Input file')

    args = parser.parse_args()

    df = pd.read_csv(args.INPUT)
    X = df.to_numpy()

    kernel_names = df.iloc[:, 0].values
    data_set_names = df.iloc[0, :].values   # these are not required...
