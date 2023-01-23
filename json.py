from dash import Dash, dcc, html
import json

# Reading json file
json_file_path = "Cars.json"
with open(json_file_path) as f:
    data = json.load(f)

# Dash App
app = Dash(__name__)

# App layout
app.layout = html.Div(
    [
        html.P("Id:"),
        dcc.Input(value=data["Id"]),
        html.P("Name:"),
        dcc.Input(value=data["Name"]),
        html.P("Price:"),
        dcc.Input(value=data["Price"]),
    ]
)

# Run Server
if __name__ == "__main__":
    app.run_server(debug=False)