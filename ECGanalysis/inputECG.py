#!/usr/bin/env python
# coding: utf-8


import scipy.io
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from io import StringIO
from datetime import date, time, datetime, timedelta


def ezsleep(filepath):
    
    F = open(filepath).read()
    data = pd.read_csv(StringIO(F),header=None)
    data = data.values.ravel().astype(np.float64)
    return data

