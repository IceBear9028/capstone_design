
import pandas as pd
import numpy as np

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask

##여기에 데이터 프레임 생성
df = pd.read_csv("capstone_design/Focus_concat.csv")
##서버(Flask), plotly 데이터 지정
server = Flask(__name__)
app = Dash(__name__, server = server)

# -> dash를 app 오브젝트로 저장함.
graph_id_1= 'graph_focus'
graph_id_2= 'grapf_nofocus'
input_id_1 = 'columns_name'

# 색깔 지정가능
colors = {
    text_1 : '#7FDBFF'
}

app.layout = html.Div([
    #1. 그래프 그리는 코어 생성
    html.Div([
        "Grapf-Focus",
        dcc.Graph(id=graph_id_1)]),
    html.Div([
        "Graph-Non_Focus",
        dcc.Graph(id=graph_id_2)]),

    #2. 그래프 input 객체 코어 생성
    html.Div([
        dcc.Dropdown(
        df.columns,
        id = input_id_1)])
    ])

@app.callback(
    Output(graph_id_1,"figure"),
    Input(input_id_1,"value")
    ) # <- 아래 update_figure의 변수로 들어감(input_1으로)
    
def update_figure(input_1):
    #여기다가 그래프 객체 선언함.
    #fig = go.Figure(data = [go.Box(y = filtered_df, boxpoints = 'all')])
    filter_df_1 = df[df['focus']==0]
    fig_1 = px.box(filter_df_1, x = input_1)
    return fig_1

@app.callback(
    Output(graph_id_2,"figure"),
    Input(input_id_1,"value")
    )

def update_figure(input_2):
    #여기다가 그래프 객체 선언함.
    #fig = go.Figure(data = [go.Box(y = filtered_df, boxpoints = 'all')])
    filter_df_2 = df[df['focus']==1]
    fig_2 = px.box(filter_df_2, x = input_2)
    return fig_2

if __name__ == '__main__':
    app.run_server(debug=True)
