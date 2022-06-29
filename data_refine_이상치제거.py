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

#df = pd.read_csv("capstone_design/Focus_concat.csv")
#df = df.drop(columns = "Unnamed: 0")

#%%
#역겨움에 대한 이상치 제거
#이 코드 쓰면 안됨!
##############
# column_idx = df.columns


# quartile_1 = df['얼굴각도'].quantile(0.25)
# quartile_3 = df['얼굴각도'].quantile(0.75)

# iqr = quartile_3 - quartile_1

# condition = (df['얼굴각도'] < (quartile_1 - 1.5 * iqr)) | (df['얼굴각도'] > (quartile_3 + 1.5 * iqr))
###############
#%%
#집중하지 않은 데이터 이상치 제거 코드
# quartile_1 = nf_df.quantile(0.25)
# quartile_3 = nf_df.quantile(0.75)

# iqr = quartile_3 - quartile_1

# condition = (nf_df < (quartile_1 - 1.5 * IQR)) | (nf_df > (quartile_3 + 1.5 * IQR))
# condition = condition.any(axis=1)

# refine_df_nf = nf_df[~condition]
# refine_df_nf['focus'] = 0
# #%%
# #집중한 데이터의 이상치 제거 코드
# quartile_1 = yf_df.quantile(0.25)
# quartile_3 = yf_df.quantile(0.75)

# iqr = quartile_3 - quartile_1

# condition = (yf_df < (quartile_1 - 1.5 * IQR)) | (yf_df > (quartile_3 + 1.5 * IQR))
# condition = condition.any(axis=1)

# refine_df_yf = yf_df[~condition]
# refine_df_yf['focus'] = 1


#%%
#1단계 : 집중하지 않은 데이터의 'a(척도)'기준 이상치 제거
a = '중앙에서벗어난정도'  # <<<<<< a에 척도 적으면 알아서 df까지 만들어줌

quartile_1 = nf_df[a].quantile(0.25)
quartile_3 = nf_df[a].quantile(0.75)

iqr = quartile_3 - quartile_1

condition = (nf_df[a] < (quartile_1 - 1.5 * iqr)) | (nf_df[a] > (quartile_3 + 1.5 * iqr))

refine_df_nf = nf_df[~condition]

# 파라미터 a의 한개의 열만 출력되게 한다.
refine_df_nf = refine_df_nf[a]
refine_df_nf = refine_df_nf.reset_index(drop = True)
refine_df_nf = refine_df_nf.rename('%s_0' %(a))


#%%
#2단계 : 집중한 데이터의 'a(척도)' 기준 이상치 제거

quartile_1 = yf_df[a].quantile(0.25)
quartile_3 = yf_df[a].quantile(0.75)

iqr = quartile_3 - quartile_1

condition = (yf_df[a] < (quartile_1 - 1.5 * iqr)) | (yf_df[a] > (quartile_3 + 1.5 * iqr))

refine_df_yf = yf_df[~condition]

# 파라미터 a의 한개의 열만 출력되게 한다.
refine_df_yf = refine_df_yf[a]
refine_df_yf = refine_df_yf.reset_index(drop = True)
refine_df_yf = refine_df_yf.rename('%s_1' %(a))


#%%
#3단계 : 집중,비집중 데이터프레임 하나로 합침.
refine_df = pd.concat([refine_df_yf,refine_df_nf],axis =1)
#그냥 concat 하면 같은 인덱스랑 붙어져서 중간중간 nan값이 나온다.

refine_df = refine_df.reset_index(drop = True)
#%%
#4단계 : 집중, 비집중 데이터 csv로 만들어준다.
refine_df.to_csv("capstone_design/%s_이상치제거concat.csv" %a)


#%%
# 집중, 비집중 데이터 이상치 따로 제거하고 합친 csv파일
#refine_df.to_csv("capstone_design/Focus_concat_refine_final.csv")

refine_df_yf.to_csv("capstone_design/Focus_refine_by화남.csv")
refine_df_nf.to_csv("capstone_design/Non_Focus_refine_by화남.csv")


#%%

refine_df = df[~condition]

#%%
refine_df.to_csv("capstone_design/%s_이상치제거concat.csv" %a)


#%%
nf_disgust_df = nf_df[['이름','역겨움']]
yf_disgust_df = yf_df[['이름','역겨움']]

