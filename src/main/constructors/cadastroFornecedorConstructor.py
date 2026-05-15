from src.view.viewCadastroFornecedor import ViewCadastroFornecedor
from src.controllers.cadastroFornecedorController import CadastroFornecedorController

def cadastroFornecedorController(page):

    telaCadastroFornecedor=ViewCadastroFornecedor(page)
    controlador=CadastroFornecedorController(page,telaCadastroFornecedor)



    return telaCadastroFornecedor