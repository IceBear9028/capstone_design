
import pandas as pd
import numpy as np

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from flask import Flask

##여기에 데이터 프레임 생성
df_focus = pd.read_csv("capstone_design/Focus.csv")
df_nonf = pd.read_csv("capstone_design/Non_Focus.csv")

df_focus["Focus_label"] = 1
df_nonf["Focus_label"] = 0

df = pd.concat([df_focus, df_nonf])

##서버(Flask), plotly 데이터 지정
server = Flask(__name__)
app = Dash(__name__, server = server)

# -> dash를 app 오브젝트로 저장함.

graph_id = 'graph_two_input'
input_id_1 = 'product'
input_id_2 = 'process_code'

app.layout = html.Div([
    #1. 그래프 그리는 코어 생성
    dcc.Graph(id=graph_id),

    #2. 그래프 input 객체 코어 생성
    dcc.Dropdown(
        df['제품코드'].unique(),
        id = input_id_1
        ),
    dcc.Dropdown(
        df.columns,
        id = input_id_2
    )
])

@app.callback(
    Output(graph_id,"figure"),
    Input(input_id_1, "value"), # <- 아래 update_figure의 변수로 들어감(input_1으로)
    Input(input_id_2, "value")
    )
def update_figure(input_1, input_2):
    filtered_df = df.loc[df['제품코드']==input_1] #전체년도데이터에서 제품코드 맞는것만 갖고옴
    # filtered_df = df_1.dropna(how = 'all',axis =1) #데이터 전체가 없는 열 삭제
    #   ㄴ--->>> 여기서 drop을 하니까 오류남.

    #여기다가 그래프 객체 선언함.
    fig = px.scatter(filtered_df, x="측정일시", y=input_2)
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
