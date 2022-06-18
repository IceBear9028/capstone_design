#test_1
import pandas as pd
import numpy as np


df_focus = pd.read_csv("capstone_design/Focus.csv")
df_nonf = pd.read_csv("capstone_design/Non_Focus.csv")

df = pd.concat([df_focus, df_nonf])
df["Focus_label"] = 1

print(df.shape)
print(df_focus.shape)
