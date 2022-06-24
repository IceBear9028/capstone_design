#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:00:13 2022

@author: isang-yun
"""

import pandas as pd
import numpy as np

#%%
df = pd.read_csv("/Users/isang-yun/dawin/통계.csv",encoding = 'utf-8')
df_1 = pd.read_csv("/Users/isang-yun/dawin/이상치 제거_통계.csv",encoding = 'utf-8')
#%%
df_2 = pd.read_csv("/Users/isang-yun/dawin/평일_설비조건정보(2021-02-01).csv",encoding = 'utf-8')

#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("dawin/통계.csv")
df_1 = pd.read_csv("dawin/이상치 제거_통계.csv")

sns.lineplot(data=df_1)