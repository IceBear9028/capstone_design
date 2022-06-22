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


# ## A. 비집중df 정제
# #1. []없애는 과정
# con_nf = nf_df['얼굴각도'].str.replace('[','')
# con_nf = con_nf.str.replace(']','')

# #2. 두개의 데이터프레임으로 나누는 과정(,기준으로 나눔)
# nf_df[['얼굴최저각도','얼굴최고각도']] = pd.DataFrame(con_nf.str.split(', ',1).tolist())

# #3. 기존 얼굴각도 날린다.
# nf_df = nf_df.drop(columns = ['얼굴각도'])

# #4. numeric이용, 각도 숫자형으로 변형
# nf_df['얼굴최저각도'] = pd.to_numeric(nf_df['얼굴최저각도'])
# nf_df['얼굴최고각도'] = pd.to_numeric(nf_df['얼굴최고각도'])

# ## B. 집중df 정제
# #1. []없애는 과정
# con_yf = yf_df['얼굴각도'].str.replace('[','')
# con_yf = con_yf.str.replace(']','')

# #2. 두개의 데이터프레임으로 나누는 과정(,기준으로 나눔)
# yf_df[['얼굴최저각도','얼굴최고각도']] = pd.DataFrame(con_yf.str.split(', ',1).tolist())

# #3. 기존 얼굴각도 날린다.
# yf_df = yf_df.drop(columns = ['얼굴각도'])

# #4. numeric이용, 각도 숫자형으로 변형
# yf_df['얼굴최저각도'] = pd.to_numeric(yf_df['얼굴최저각도'])
# yf_df['얼굴최고각도'] = pd.to_numeric(yf_df['얼굴최고각도'])


## C. 인덱스 부착,두 df 합침
nf_df["focus"] = 0
yf_df["focus"] = 1


df = pd.concat([yf_df, nf_df])
df = df.reset_index(drop = True)
df['얼굴각도'] = df['얼굴각도'].round(3)


## D. 얼굴각도 차이 계산, 최종df 완성
# angle_dif = df['얼굴최고각도'] - df['얼굴최저각도']
# angle_dif = angle_dif.round(3)
# df.insert(12,'얼굴각도차이', angle_dif)



## E. 최종df 추출
df.to_csv("capstone_design/Focus_concat.csv")


df_sad = pd.concat([df['슬픔'],df['focus']],axis = 1)
df_sad = df_sad.reset_index(drop = True)
#drop해줘야지 이전 인덱스값 안남음.
df_sad = df_sad.rename(columns = {'슬픔':'sad'})

#####ㅅㅣ발시발시발개시발 
#####column 이름 영어 아니면 drop, 추출 이런거 하나도 안먹힘.
#####꼭 column이름 영어로 변환할 것.

#sad_idx = df_sad[df_sad['sad']>0.4].index
#df_sad = df_sad.drop(index = sad_idx)
df_sad = df_sad[df_sad.sad < 0.4]


corr = df_sad.corr(method = 'pearson')
corr = df.corr(method = 'pearson')
#print(df_sad.head(),df_sad.tail(),df_sad.shape)


