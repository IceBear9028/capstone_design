import pandas as pd
import numpy as np

import plotly.express as px

before_df = pd.read_csv("capstone_design/Focus_concat_sorting.csv")

before_df_1 = before_df.drop(['구간순서'], axis = 1)

df = before_df_1#[before_df_1['이름'] == '곽민상']

fig = px.parallel_coordinates(df, color="focus", 
                    color_continuous_scale=px.colors.diverging.Tealrose)
fig.show()