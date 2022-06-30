
import pandas as pd
import numpy as np

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask

##여기에 데이터 프레임 생성
df = pd.read_csv("capstone_design/Focus_concat_sorting.csv")
##서버(Flask), plotly 데이터 지정
server = Flask(__name__)
app = Dash(__name__, server = server)

# -> dash를 app 오브젝트로 저장함.
graph_id_2= 'graph_box'
graph_id_3= 'graph-scatter_y'
graph_id_4= 'graph-scatter_N'
graph_id_5= 'graph-scatter_y_'
graph_id_6= 'graph-scatter_N_'
graph_id_7= 'user_scatter'

input_id_1 = 'columns_name'
input_id_2 = 'columns_name_'
input_id_3 = 'columns_name_1'
input_id_4 = 'columns_name_2'
input_id_5 = 'user_name'
#input_id_6 = 'user_columns'

# 색깔 지정가능

app.layout = html.Div(
    className = "main", 
    children = [
    html.Div(
        className = "box-plot",
        children = [
        html.H1("Box-plot", className = 'headTitle'),
        html.Div(
            className="box-plot-graph",
            children = [dcc.Graph(id = graph_id_2)]
        ),
        html.Div(
            className = 'box-plot-input',
            children = [html.H3("select category", className = "selectTitle"),
                        dcc.Dropdown(df.columns,"중립",id = input_id_1)]
        )
    ]),

    html.Div(
        className = "scatter-plot",
        children = [
        html.H1("Scatter-plot(학습자)", className = 'headTitle'),
        html.Div(
            className = "scatter-plot-graph",
            children = [
                html.H2("집중한 사람", className = "subTitle"),
                html.Div(
                    className = "scatter-plot-graph1",
                    children = [dcc.Graph(id = graph_id_3)]
                ),
                html.H2("집중하지 않은 사람", className = "subTitle"),
                html.Div(
                    className = "scatter-plot-graph2",
                    children = [dcc.Graph(id = graph_id_4)]
                ),
                html.Div(
                    className = 'scatter-plot-input',
                    children = [html.H3("input", className = "selectTitle"),
                                dcc.Dropdown(df.columns,"행복",id = input_id_2)]
                )
            ]
        )
    ]),

    html.Div([
        html.Div(
            className = 'scatter-plot2',
            children = [
                html.H1("scatter - 2개 척도별 확인"),
                html.H2("집중한 사람", className = "subTitle"),
                html.Div(
                    className = "scatter-plot2-graph1",
                    children = [dcc.Graph(id = graph_id_5)]
                ),
                html.H2("집중하지 않은 사람", className = "subTitle"),
                html.Div(
                    className = "scatter-plot2-graph2",
                    children = [dcc.Graph(id = graph_id_6)]
                ),
                html.Div(
                    className = "selectTitle",
                    children = [html.H3("척도 1", className = 'selectTitle'),
                                dcc.Dropdown(df.columns,"Unnamed: 0",id = input_id_3)]
                ),
                html.Div(
                    className = "selectTitle",
                    children = [html.H3("척도 2", className = "selectTitle"),
                                dcc.Dropdown(df.columns,"중립",id = input_id_4)]
                )
            ]
        )
    ]),

    html.Div([
        html.Div(
            className = "corr",
            children = [
                html.H1("각 학습자간의 척도관계도"),
                html.Div(
                    className = "corr-graph",
                    children = [dcc.Graph(id = graph_id_7)]
                ),
                html.Div(
                    className = "selectTitle",
                    children = [html.H3("학습자 이름", className = "selectTitle"),
                                dcc.Dropdown(df['이름'].unique(),"곽민상",id = input_id_5)]
                )
            ]
        )
    ])
])

    #2. 그래프 input 객체 코어 생성

@app.callback(
    Output(graph_id_2,"figure"),
    Input(input_id_1,"value")
    ) # <- 아래 update_figure의 변수로 들어감(input_1으로)
    
def update_figure_box(input_1):
    fig_2 = px.box(df, x = 'focus', y = input_1, points = 'all')

    fig_2.update_layout(height = 1020)

    return fig_2

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

@app.callback(
    Output(graph_id_5,"figure"),
    Output(graph_id_6,"figure"),
    Input(input_id_3,"value"),
    Input(input_id_4,"value")
    )  

def update_figure_scatter(input_1,input_2):
    filter_df_1 = df[df['focus']==1]
    filter_df_2 = df[df['focus']==0]

    fig_1 = px.scatter(filter_df_1, x= input_1, y = input_2)
    fig_2 = px.scatter(filter_df_2, x= input_1, y = input_2)
    
    return fig_1, fig_2

@app.callback(
    Output(graph_id_7,"figure"),
    Input(input_id_5,"value")
)

def corr_graph(input):
    user_df = df[df['이름'] == input]
    filter_df = user_df.drop(['구간순서'], axis = 1)
    
    fig = px.parallel_coordinates(
        filter_df, color = 'focus',color_continuous_scale=px.colors.diverging.Tealrose)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
