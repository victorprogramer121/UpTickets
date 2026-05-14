from src.view.viewCadastroUsuario import ViewCadastroUsuario
from src.controllers.cadastroUsuarioController import CadastroUsuarioController

def cadastroUsuarioConstructor(page):

    telaCadastroUsuario=ViewCadastroUsuario(page)
    controlador=CadastroUsuarioController(page,telaCadastroUsuario)



    return telaCadastroUsuario