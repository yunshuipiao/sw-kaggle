#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: mat.py

@desc:

@hint:
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('../../lagou/sz.csv')


train['city'].value_counts().plot.bar()
