from src.model.entitys.evento import Evento
from src.model.DAO.evento import Eventos_DAO
from src.infrastructure.services.geradorID import GeradorID
from src.view.viewLogin import ViewLogin
from src.view.viewCadastroFornecedor import ViewCadastroFornecedor
from src.view.viewCadastroUsuario import ViewCadastroUsuario
from src.model.entitys.usuario import Usuario
from src.model.DAO.usuario import UsuarioDAO
from src.model.entitys.fornecedor import Fornecedor
from src.model.DAO.fornecedor import FornecedorDAO
from flet import *


class ViewController:

    def __init__(self,page,tela:ViewLogin):
        self.daoEvento=Eventos_DAO()
        self.page=page
        self.telaLogin=tela
        #self.listarEventos()
        self.telaLogin.btnEntrarUsuario.on_click=self.trocaTelaUsuario
        self.telaLogin.btnEntrarFornecedor.on_click=self.trocaTelaFornecedor
        self.telaLogin.cadastroUsuario.on_click=self.trocaTelacadastroUsuario
        self.telaLogin.cadastroFornecedor.on_click=self.trocaTelacadastroFornecedor


        self.page.update()


    def trocaTelaUsuario(self,e)->None:
        
        if len (self.telaLogin.email.value)==0:
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
    
    def trocaTelaFornecedor(self,e)->None:
            if len(self.telaLogin.cnpj.value)==0:
                self.telaLogin.cnpj.error="Você precisa digitar o login"
                self.telaLogin.cnpj.update()
                
            else:
                self.telaLogin.cnpj.error=""
                self.telaLogin.cnpj.update()
                
                if  len(self.telaLogin.password.value)>0:
                    
                    self.page.go("/inicial")
                    
                else:
                    self.telaLogin.password.error="senha ou cnpj esta incorreta"
                    self.telaLogin.password.update()
                    


    def trocaTelacadastroUsuario(self,e)->None:
            self.page.go("cadastroUsuario")
            self.page.update()



    def trocaTelacadastroFornecedor(self,e)->None:
        self.page.go("/cadastroFornecedor")
        self.page.update()
        

        




    def listarEventos(self)->None:
        self.tela.limparLista.rows.clear()
        caixa=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            Image(src="src/view/imagens/party.jpg"),
                            Image(src="src/view/imagens/videogame.jpg"),
                            Image(src="src/view/imagens/reuniao.jpg")
                        ]
                    ),
                    ResponsiveRow(
                        controls=[

                        ]
                    )
                ]
                    
                
            )
            
        )
        self.tela.page.add(caixa)
        
        opcao=input("escolha a imagem do seu evento")
        match opcao:

            case "1":
                        
                for evento in self.dao.lerEventos():
                    caixa=Container(
                        content=Column(
                            controls=[
                                ResponsiveRow(controls=[Image(src="src\view\imagens\party.jpg")
                                    
                                    
                                ]
                                )
                            ]
                        )
                    )
                


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
    


    
