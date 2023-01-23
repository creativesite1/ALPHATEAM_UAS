import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import Cars.xml as mod

cnxn = mod.connect("Cars.xml")

df = pd.read_sql("SELECT [ Model ], [ Price] FROM people WHERE [id]", cnxn)
app_name = 'dash-xmldataplot'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'CData + Dash'
trace = go.Bar(x=df[ Model ], y=df[ Price], name='[ id ]')

app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
	dcc.Graph(
		id='example-graph',
		figure={
			'data': [trace],
			'layout':
			go.Layout(title='XML people Data', barmode='stack')
		})
], className="container")

if __name__ == '__main__':
    app.run_server(debug=False)
