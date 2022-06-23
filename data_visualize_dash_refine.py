
import pandas as pd
import numpy as np

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask

##여기에 데이터 프레임 생성
df = pd.read_csv("capstone_design/Focus_concat_refine.csv")
##서버(Flask), plotly 데이터 지정
server = Flask(__name__)
app = Dash(__name__, server = server)

# -> dash를 app 오브젝트로 저장함.
graph_id_1= 'graph_focus'
graph_id_2= 'grapf_nofocus'
graph_id_3= 'graph-scatter_y'
graph_id_4= 'graph-scatter_N'

input_id_1 = 'columns_name'
input_id_2 = 'columns_name_'
# 색깔 지정가능

app.layout = html.Div([

    #1. 그래프 그리는 코어 생성
    html.Div([
        "Graph-Box",
        dcc.Graph(id=graph_id_1),
        dcc.Graph(id=graph_id_2),
        dcc.Dropdown(
            df.columns,
            id = input_id_1)
        ]),
    
    html.Div([
        "Scatter-by.person",
        html.H2("집중한 사람"),
        dcc.Graph(id=graph_id_3),
        html.H2("집중하지 않은 사람"),
        dcc.Graph(id=graph_id_4),
        dcc.Dropdown(
            df.columns,
            id = input_id_2)
        ])
])

    #2. 그래프 input 객체 코어 생성

@app.callback(
    Output(graph_id_1,"figure"),
    Output(graph_id_2,"figure"),
    Input(input_id_1,"value")
    ) # <- 아래 update_figure의 변수로 들어감(input_1으로)
    
def update_figure_box(input_1):
    filter_df_1 = df[df['focus']==1]
    filter_df_2 = df[df['focus']==0]

    fig_1 = px.box(filter_df_1, x = input_1)
    fig_2 = px.box(filter_df_2, x = input_1)

    return fig_1,fig_2

@app.callback(
    Output(graph_id_3,"figure"),
    Output(graph_id_4,"figure"),
    Input(input_id_2,"value")
    )

def update_figure(input):
    filter_df_1 = df[df['focus']==1]
    filter_df_2 = df[df['focus']==0]

    fig_1 = px.scatter(filter_df_1, x= "이름",y = input)
    fig_2 = px.scatter(filter_df_2, x="이름",y = input)
    
    return fig_1, fig_2


if __name__ == '__main__':
    app.run_server(debug=True)
