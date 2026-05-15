from src.view.viewInicial import ViewInicial

from src.controllers.cadastroTelaEvento import ViewInicialController

def CadastroTelaConstructor(page):
    telaInicialController=ViewInicial(page)
    controlador=ViewInicialController(page,telaInicialController)



    return telaInicialController