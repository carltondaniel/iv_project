# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('/home/carlton/Downloads/vgsales.csv')
df.dropna(inplace = True)



app.layout = html.Div(children=[
    
    
dcc.Dropdown(
    options=[
        {'label': 'Name', 'value': 'Name'},
        {'label': 'Platform', 'value': 'Platform'},
        {'label': 'Genre', 'value': 'Genre'},
        {'label': 'Publisher', 'value': 'Publisher'}
    ],
    id='category',
    value='Platform'
),  
    dcc.Dropdown(
    options=[
        {'label': 'NA_Sales', 'value': 'NA_Sales'},
        {'label': 'EU_Sales', 'value': 'EU_Sales'},
        {'label': 'JP_Sales', 'value': 'JP_Sales'},
        {'label': 'Other_Sales', 'value': 'Other_Sales'},
        {'label': 'Global_Sales', 'value': 'Global_Sales'}
    ],
    id='num',
    value='NA_Sales'
),
   dcc.Loading(
    children=dcc.Graph(
    id='graph-1'
        
    )
    ),
      dcc.Loading(
    children=dcc.Graph(
    id='graph-2'
        
    )
    )
])

@app.callback(
    Output('graph-1', 'figure'),
    [Input('category', 'value'),
    Input('num', 'value')]  )
def update_figure(selected_category,selected_numeric):
    # print('Hello')
    # print(selected_category)
    # print(selected_numeric)
    fig = px.bar(df, x=selected_category, y=selected_numeric,barmode="group")

 

    return fig

@app.callback(
    Output('graph-2', 'figure'),
    [Input('category', 'value'),
    Input('num', 'value')]  )
def update_figure(selected_category,selected_numeric):
    # print('Hello')
    # print(selected_category)
    # print(selected_numeric)
    fig = px.pie(df,names=selected_category, values=selected_numeric)

 

    return fig




if __name__ == '__main__':
    app.run_server(debug=True,port=8015)  