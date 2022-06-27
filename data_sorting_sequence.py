#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:27:30 2022

@author: isang-yun
"""

import pandas as pd
import numpy as np
#%%
yf_df = pd.read_csv("Focus.csv", encoding = 'cp949')
nf_df = pd.read_csv("Non_Focus.csv", encoding = 'cp949')
#%%
# yf_df 열 이름 교체
yf_con_df_mp4 = yf_df['이름'].str.replace('.mp4','')

#yf_df 이름에 .mp4 문자열을 없애주는 작업
yf_df['이름'] = yf_con_df_mp4

#%%

#1. df['이름'] 의 "이름_집중여부(1,0)_구간순서(1~21)" 을 다른 3개의 열로 쪼개는 작업
yf_df[['이름','focus','구간순서']] = pd.DataFrame(yf_df['이름'].str.split('_',2).tolist())
#%%
#2. 쪼갠 3개 중 2개의 열을 숫자형으로 변환
yf_df['focus'] = pd.to_numeric(yf_df['focus'])
yf_df['구간순서'] = pd.to_numeric(yf_df['구간순서'])
#%%
#3. 1과정과 마찬가지로 3개의 데이터 열로 쪼개는 작업 
nf_df[['이름','focus','구간순서']] = pd.DataFrame(nf_df['이름'].str.split('_',2).tolist())

#%%
#4. 2과정과 마찬가지로 숫자형으로 변환
nf_df['focus'] = pd.to_numeric(nf_df['focus'])
nf_df['구간순서'] = pd.to_numeric(nf_df['구간순서'])


#%%
#5. nf_df, yf_df를 concat
concat_df = pd.concat([yf_df, nf_df])
# +++ '구간순서'의 데이터들이 몇개 있나 확인해보기 위함.
concat_df_unique = concat_df['구간순서'].unique()

#6. 합친 데이터를 '이름'기준의 그룹으로 만들어서 '구간순서'를 숫자형으로 오름차순으로 정렬시킴.
sorting_df = concat_df.groupby(['이름']).apply(lambda x:x.sort_values(['구간순서'])).reset_index(drop = True)
##내림차순정렬시, sort_value(ascending = False) 를 넣어주면 된디.

#%%
###최종 데이터프레임을 csv로 저장함.
sorting_df.to_csv('Focus_concat_sorting.csv')
