from src.main.constructors.produtoConstructor import produtoConstructor
from flet import *


def app(page:Page):
    page.title="controle de eventos"


    def changeRoute():
        page.views.clear()
        page.views.append(produtoConstructor(page))
        page.update()

    page.on_route_change=changeRoute
    changeRoute()
    page.go(page.route)