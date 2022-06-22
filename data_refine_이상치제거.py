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

#%%
#역겨움에 대한 이상치 제거
nf_disgust_df = nf_df[['이름','역겨움']]
yf_disgust_df = yf_df[['이름','역겨움']]

