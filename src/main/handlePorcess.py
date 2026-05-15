from src.main.constructors.produtoConstructor import produtoConstructor
from src.main.constructors.cadastroUsuarioConstructor import CadastroTelaConstructor
from flet import *


def app(page:Page):
    page.title="controle de eventos"
    


    def changeRoute(e=None):
        page.views.clear()
        page.views.append(
            produtoConstructor(page)
                          )
      

        if page.route=="/inicial":
            
            page.views.append(
                CadastroTelaConstructor(page)
            )
        page.update()

    page.on_route_change=changeRoute
    changeRoute()
    page.go(page.route)