#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 20:10:32 2022

@author: isang-yun
"""

import pandas as pd
import numpy as np
#%%
df = pd.read_csv("상관관계.csv" , encoding = 'cp949')
#%%
df.info()
#%%

# 상관관계(pearson)
# 0 < corr < 0.2 => very pool
# 0.2 < corr < 0.4 => pool
# 0.4 < corr < 0.6 => 

def corr_discrimination(corr):
    abs_corr = abs(corr)
    if abs_corr > 0.2:
        if abs_corr > 0.4:
            if abs_corr > 0.6:
                if abs_corr > 0.85:
                    if abs_corr == 1:
                        return None
                    else:
                        return "매우강한상관관계"
                else:
                    return "높은상관관계"
            else:
                return "다소높은상관관계"
        else:
            return "낮은상관관계"
    else:
        return "매우낮은상관관계"


#%%
df_discrimination = df.drop(['Unnamed: 0'], axis = 'columns')

for i in df_discrimination.columns:
    df_discrimination[i] = df_discrimination[i].apply(corr_discrimination)

