#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:41:35 2022

@author: isang-yun
"""

import pandas as pd
import numpy as np



#%%
non_df = pd.read_csv("Non_Focus.csv")
y_df = pd.read_csv("Focus.csv")
#%%
non_df["focus"] = 0
y_df["focus"] = 1

df = pd.concat([y_df, non_df])
#%%
df_cor = df.corr(method = 'pearson')
