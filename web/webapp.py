# run cmd 
# python3 webapp.py

import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv('webdata.csv', header = 0, delimiter=',', encoding='unicode_escape')
# print(df.info())

app = Dash(__name__)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[

    html.H1(children='Hello Dash 2'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
