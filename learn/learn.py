# -*- coding: utf-8 -*-
# import click

from functools import reduce
import sys
import math
import os
import re

fpath = '.\\ky\\data\\data.csv'


def log(s):
    print(re.split(r'[\,\s]+', s.strip()))


def hello():
    with open(fpath, 'r', errors='ignore') as f:
        for s in f.readlines():
            log(s)
    # print(re.split(r'[\s\,]+', 'a,bc,d\n'.strip()))


if __name__ == '__main__':
    hello()
