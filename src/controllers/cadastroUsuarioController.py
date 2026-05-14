from src.model.DAO.usuario import UsuarioDAO
from src.model.entitys.usuario import Usuario
from src.view.viewCadastroUsuario import ViewCadastroUsuario
from flet import *


    


class CadastroUsuarioController:

    def __init__(self, page,tela:ViewCadastroUsuario):
        
        self.daoUsuario=UsuarioDAO()
        self.page=page
        self.telaUsuario=tela
        self.telaUsuario.btnCadastro=self.trocaTelaInicial


    

    def trocaTelaInicial(self,e):
        self.page.go("/inicial")

    

    def cadastroUsuario(self,e):
        u=Usuario(
            self.telaUsuario.nome.value,
            self.telaUsuario.email.value,
            self.telaUsuario.cadastrarPassword.value


        )
        try:
            self.daoUsuario.addUsuario(u.usuarioDict)


            self.telaUsuario.email.update()
            self.telaUsuario.cadastrarPassword.update()

            
        except Exception as e :
            print(e)

