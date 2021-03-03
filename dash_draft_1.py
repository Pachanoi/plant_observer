# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:56:57 2021

@author: chmoo
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv('https://raw.githubusercontent.com/Pachanoi/data/main/dupa.csv')
df = df.drop(index=491) #drops that one row with repeated column names
df = df.astype({'Temperature':float, 'Pressure':float, 'Humidity':float})
df.Time = df.Time.apply(lambda x : dt.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
df.dtypes

'''
matplotlib staff for quick visualisation
df2 = df[::20]


fig = plt.figure()
ax = fig.add_subplot()
ax.plot(df2.Time, df2.Pressure)
#ax.set_ylim([1015,1025])
plt.show()
'''
app = dash.Dash(__name__)
# App layout

app.layout = html.Div([
    html.H1("Test", style={'text-align':'center'}),
    dcc.RadioItems(id = 'radio_buttons', options=[
        {'label' : 'Temperature', 'value' : 'Temperature'},
        {'label' : 'Pressure', 'value' : 'Pressure'},
        {'label' : 'Humidity', 'value' : 'Humidity'}],
        value = 'Temperature'),
    

    
    
    html.Br(),
    
    dcc.Graph(id='plant_graph', figure=px.scatter(df, x='Time', y='Temperature'))
])

@app.callback(
    Output('plant_graph', 'figure'),
    Input('radio_buttons', 'value'))
def update_figure(column):
    fig = px.scatter(df, x="Time", y=column)

    return fig


if __name__ == '__main__':
    # print(stock_df)
    app.run_server(debug=True)
