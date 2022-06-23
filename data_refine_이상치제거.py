#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:41:35 2022

@author: isang-yun
"""

import pandas as pd
import numpy as np

nf_df = pd.read_csv("capstone_design/Non_Focus.csv",encoding = 'cp949')
yf_df = pd.read_csv("capstone_design/Focus.csv", encoding = 'cp949')

df = pd.read_csv("capstone_design/Focus_concat.csv")
df = df.drop(columns = "Unnamed: 0")

#%%
#역겨움에 대한 이상치 제거
column_idx = df.columns


quartile_1 = df.quantile(0.25)
quartile_3 = df.quantile(0.75)

IQR = quartile_3 - quartile_1

condition = (df < (quartile_1 - 1.5 * IQR)) | (df > (quartile_3 + 1.5 * IQR))
condition = condition.any(axis=1)

refine_df = df[condition]

refine_df.to_csv("capstone_design/Focus_concat_refine.csv")


#%%
nf_disgust_df = nf_df[['이름','역겨움']]
yf_disgust_df = yf_df[['이름','역겨움']]

