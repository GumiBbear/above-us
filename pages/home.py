import dash
from dash import html

dash.register_page(__name__, path="/", name="Главная")

layout = html.Div([ 
    html.H1("Главная"),
    html.P("Пока нет текста"),
])


