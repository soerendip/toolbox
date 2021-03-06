import pandas as pd
import numpy as np
import os, re

from datetime import date
from os.path import isdir, isfile, basename, dirname, join
from time import sleep
from glob import glob
from pathlib import Path as P
from tqdm.notebook import tqdm

import seaborn as sns

from matplotlib import pyplot as plt

plt.rcParams['figure.facecolor'] = 'w'
plt.rcParams['figure.dpi'] = 150

pd.options.display.max_colwidth = 100
pd.options.display.max_columns = 100


def today():
    return date.today().strftime('%y%m%d')

# STOP

from . import tools

with open(__file__, 'r') as this_file:
    for line in this_file.readlines():
        if re.search('STOP', line):
            break
        print(line, end="")
