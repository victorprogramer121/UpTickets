
from src.model.DAO.evento import Eventos_DAO
from src.view.viewLogin import ViewLogin




from flet import *


class ViewController:

    def __init__(self,page,tela:ViewLogin):
        self.daoEvento=Eventos_DAO()
       
        self.daoUsuario=UsuarioDAO()
        
       
        self.page=page
        self.telaLogin=tela
        #self.listarEventos()
        self.telaLogin.btnEntrarUsuario.on_click=self.trocaTelaUsuario
        
      



        self.page.update()


    def trocaTelaUsuario(self,e)->None:
        
        if len (self.telaLogin.email.value)=="@":
            self.telaLogin.email.error="Você precisa digitar o login"
            self.page.update()
        else:
            self.telaLogin.email.error=""
            self.page.update()
            if  len(self.telaLogin.password.value)>0:
                self.page.go("/inicial")
            else:
                self.telaLogin.password.error="senha ou email esta incorreta"
                self.page.update()
    




    def buscarEvento(self, id:int):
        try:
            return self.dao.buscarPorID(id)
        except Exception as e:
            return e
from src.model.DAO.databaseDB import DatabaseDB





    


class UsuarioDAO:

    def init(self):
        self.conn=DatabaseDB("usuarios.json")


    def addUsuario(self,dados:dict):
        try:
            self.conn.salvar(dados)
            return f"usuario salvo com sucesso"
        except Exception as e:
            raise ValueError("erro na hora de salva fdp desgracado, salva essa porra de novo, jumento",e)


    def deletarUsuario(self,nomeUsuario):
        novoUsuario=[usuario for usuario in self.lerUsuario() if usuario["email"]!=nomeUsuario]
        if len(novoUsuario)==len(self.lerUsuario()):
            raise ValueError("nenhum usuario encontrado")
        self.conn.historicoCadastro(novoUsuario)
        print("deletado com sucesso")


    def lerUsuario(self):
        return self.conn.lerArquivo()
    


    
