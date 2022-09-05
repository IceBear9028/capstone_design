import pandas as pd
import numpy as np

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask

df = pd.read_csv("capstone_design/Focus_concat_sorting.csv")

server = Flask(__name__)
app = Dash(__name__, server = server)

graph_id_1= 'graph_eye_l'
graph_id_2= 'graph-eye_r'

app.layout = html.Div([
    html.H4('눈깜빡임 확률_왼쪽'),
    dcc.Graph(id = graph_id_1),
    dcc.Graph(id = graph_id_2)
])


@app.callback(
    Output(graph_id_1, "figure")
    Output(graph_id_2, "figure")
)

def graph_left_eye(continents):
    fig = px.line(df['깜빡임확률 l'], 
        x="Unnamed: 0", y='깜빡임확률 l')
    return fig

def graph_left_eye(continents):
    fig = px.line(df['깜빡임확률 r'], 
        x="Unnamed: 0", y='깜빡임확률 r')
    return fig

app.run_server(debug=True)