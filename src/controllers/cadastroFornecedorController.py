from flet import *
from src.model.DAO.fornecedor import FornecedorDAO
from src.model.entitys.fornecedor import Fornecedor
from src.view.viewCadastroFornecedor import ViewCadastroFornecedor
 
 
 
 
class CadastroFornecedorController:
    def __init__(self,page,tela:ViewCadastroFornecedor):

        self.daoFornecedor=FornecedorDAO()
        self.page=page
        self.telaFornecedor=tela
        self.telaFornecedor.btnCadastro=self.trocaTelaInicial
 
 
 
    def trocaTelaInicial(self,e):
        self.page.go("/inicial")
        self.page.update()
 
   
    def cadastroFornecedor(self,e):
       
        f=Fornecedor(
 
            self.telaFornecedor.nome.value,
            self.telaFornecedor.cnpj.value,
            self.telaFornecedor.cadastrarPassword.value
 
        )
        try:
            self.daoFornecedor.addFornecedor(f.fornecedorDict)
 
            self.telaFornecedor.nome.update()
            self.telaFornecedor.cnpj.update()
            self.telaFornecedor.cadastrarPassword.update()
 
 
        except Exception as e:
            print(e)
 
 