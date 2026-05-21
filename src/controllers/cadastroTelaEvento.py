from src.view.viewInicial import ViewInicial
from src.model.DAO.evento import Eventos_DAO
from src.model.entitys.evento import Evento
from src.infrastructure.services.geradorID import GeradorID
import flet as ft


class ViewInicialController:

    def __init__(self,page,tela:ViewInicial):

        self.dao=Eventos_DAO()
        self.page=page
        self.tela=tela
        self.tela.btnADD.on_click=self.addEvento
        self.listarEventos(atualizar_tela=False)




        
    def listarEventos(self,atualizar_tela=False):
        self.tela.tabelaEvento.content.controls.clear()
        
        for produto in self.dao.visualizarEvento():
            cartao_evento = ft.Card(
                elevation=5, 
                content=ft.Container(
                    padding=15,
                    bgcolor=ft.Colors.GREY_100,
                    border_radius=10,
                    content=ft.Row(
                        controls=[
                           
                            ft.Image(
                                src=produto["imagem"], 
                                width=150, 
                                height=150, 
                                fit="cover",
                                border_radius=10
                                
                                
                            ),
                            
                            ft.Column(
                                controls=[
                                    ft.Text(f"ID: {produto['id']}", size=12, color=ft.Colors.BLACK),
                                    ft.Text(f"Evento: {produto['nomeEvento']}", size=20, weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK),
                                    ft.Text(f"Local: {produto['local']}", size=16,color=ft.Colors.BLACK),
                                    ft.Text(f"Data: {produto['data']}", size=16, color=ft.Colors.BLUE_900),
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START
                    )
                )
            )
            self.tela.tabelaEvento.content.controls.append(cartao_evento)
        
        if atualizar_tela:
            self.tela.update()

           

    def addEvento(self,e):
        
        e= Evento(
            GeradorID("eventos.json","id").id_gerado,
        
            nomeEvento=self.tela.nomeEvento.value,
            imagem="src/view/imagens/party.jpg",
            local=self.tela.local.value,
            data=self.tela.data.value
        )
        try:
            self.dao.addEventos(e.eventoDict())


            self.tela.nomeEvento.value=""
            self.tela.local.value=""
            self.tela.data.value=""


            self.tela.nomeEvento.update()
            self.tela.local.update()
            self.tela.data.update()
        
            self.listarEventos(atualizar_tela=True)

            self.tela.controls=self.tela.layout_inicial
            self.tela.update()

        except Exception as e:
            print(e)






    def voltarTela(self,e):
        self.page.go("/")




