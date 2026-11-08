import dash_bootstrap_components as dbc

def create_navbar():
    return dbc.NavbarSimple(
        children = [
            dbc.NavItem(dbc.NavLink("Главная", href="/")),

            dbc.NavItem(dbc.NavLink("Фото дня NASA", href="/apod")),
            dbc.NavItem(dbc.NavLink("Новости и события", href="/news")),
            dbc.NavItem(dbc.NavLink("Справочник объектов", href="/directory")),
            dbc.NavItem(dbc.NavLink("Интерактивная карта неба", href="/i-map")),
            dbc.NavItem(dbc.NavLink("Отслеживание МКС в реальном времени", href="/tracking-mks")),
            dbc.NavItem(dbc.NavLink("Генерация карты неба по дате", href="/gen-map")),
            dbc.NavItem(dbc.NavLink("Астрономический календарь", href="/calendar")),
        ],

        brand="Above Us",
    )

