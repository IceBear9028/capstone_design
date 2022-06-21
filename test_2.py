import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("capstone_design/Focus_concat.csv")
index = df.columns
fig = px.box(df,y = index )
fig.show()

