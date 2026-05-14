from src.main.constructors.produtoConstructor import produtoConstructor
from src.view.viewCadastroFornecedor import ViewCadastroFornecedor
from src.view.viewCadastroUsuario import ViewCadastroUsuario
from src.view.viewInicial import ViewInicial
from flet import *


def app(page:Page):
    page.title="controle de eventos"


    def changeRoute(e=None):
        page.views.clear()
        page.views.append(
            produtoConstructor(page)
                          )
        if page.route=="/cadastroFornecedor":
            page.views.append(
                ViewCadastroFornecedor(page)
        )
        

        if page.route=="/cadastroUsuario":
            page.views.append(
                ViewCadastroUsuario(page)
            )

        if page.route=="/inicial":
            page.views.append(
                ViewInicial(page)
            )
        page.update()

    page.on_route_change=changeRoute
    changeRoute()
    page.go(page.route)