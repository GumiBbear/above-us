import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([ 
    html.H1("Фото дня NASA"),
    html.P("Пока нет текста"),
])