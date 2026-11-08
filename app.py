import dash
from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
from components.navbar import create_navbar


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])
app.layout = html.Div([
    create_navbar(),
    page_container,
    
])

if __name__ == '__main__':
    app.run(debug=True)

