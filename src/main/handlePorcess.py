from src.main.constructors.produtoConstructor import produtoConstructor
from src.main.constructors.cadastroUsuarioConstructor import cadastroUsuarioConstructor
from src.main.constructors.cadastroFornecedorConstructor import cadastroFornecedorController
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
            page.views.clear()
            page.views.append(
                cadastroFornecedorController(page)
        )
        

        if page.route=="/cadastroUsuario":
            page.views.clear()
            page.views.append(
                cadastroUsuarioConstructor(page)
            )

        if page.route=="/inicial":
            page.views.clear()
            page.views.append(
                CadastroTelaConstructor(page)
            )
        page.update()

    page.on_route_change=changeRoute
    changeRoute()
    page.go(page.route)