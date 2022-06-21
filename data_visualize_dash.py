
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
graph_id = 'graph_input'
input_id_1 = 'columns_name'


app.layout = html.Div([
    #1. 그래프 그리는 코어 생성
    dcc.Graph(id=graph_id),

    #2. 그래프 input 객체 코어 생성
    dcc.Dropdown(
        df.columns,
        id = input_id_1
    )
])

@app.callback(
    Output(graph_id,"figure"),
    Input(input_id_1,"value")
    ) # <- 아래 update_figure의 변수로 들어감(input_1으로)
    
def update_figure(input_1):
    #여기다가 그래프 객체 선언함.
    #fig = go.Figure(data = [go.Box(y = filtered_df, boxpoints = 'all')])
    fig = px.box(df, x = input_1)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
