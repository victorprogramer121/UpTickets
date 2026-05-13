from src.model.entitys.evento import Evento
from src.model.DAO.evento import Eventos_DAO
from src.infrastructure.services.geradorID import GeradorID
from src.view.viewLogin import ViewLogin
from src.view.viewCadastroFornecedor import ViewCadastroFornecedor
from src.view.viewCadastroUsuario import ViewCadastroUsuario
from flet import *


class ViewController:

    def init(self,page,tela:ViewLogin):
        self.dao=Eventos_DAO()


        self.page=page
        self.tela=tela
        self.listarEventos()
        self.btnEntrarUsuario.on_click=self.trocaTelaUsuario
        self.btnEntrarFornecedor.on_click=self.trocaTelaFornecedor
        self.cadastroUsuario.on_click=self.trocaTelacadastroUsuario
        self.cadastroFornecedor=self.trocaTelacadastroFornecedor


    def trocaTelaUsuario(self)->None:
        if len (self.email.value)==0:
            self.email.error="Você precisa digitar o login"
            self.email.update()
        else:
            self.email.error=""
            self.email.update()
            if self.email.value>0 and self.password>0:
                self.pagina.go("/inicial")
            else:
                self.password.error="senha ou email esta incorreta"
                self.password.update
    
    def trocaTelaFornecedor(self)->None:
            if len (self.cnpj.value)==0:
                self.cnpj.error="Você precisa digitar o login"
                self.cnpj.update()
            else:
                self.cnpj.error=""
                self.cnpj.update()
                if self.cnpj.value>0 and self.password>0:
                    self.pagina.go("/inicial")
                else:
                    self.password.error="senha ou email esta incorreta"
                    self.password.update


    def trocaTelacadastroUsuario(self)->None:
        self.pagina.go("/cadastroUsuario")


    def trocaTelacadastroFornecedor(self)->None:
        self.pagina.go("/cadastroFornecedor")
        

        




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
    


    
