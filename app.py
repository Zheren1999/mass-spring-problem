from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from spring_mass_problem import SpringMassProblem

app = Dash(__name__)

t, d = SpringMassProblem.get_solution(10, 1)

df = pd.DataFrame({
    "t": t,
    "d": d,
})

fig = px.scatter(df, x="t", y="d")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)