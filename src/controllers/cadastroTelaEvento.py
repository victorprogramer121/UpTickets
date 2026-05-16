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
        self.listarEventos()




        
    def listarEventos(self):
        self.tela.tabelaEvento.content.controls.clear()
        for produto in self.dao.visualizarEvento():
            linha=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                ft.Text(produto["id"])
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Image(src=produto["src/view/imagens/party.jpg"])
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Text(produto["nomeEvento"])
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Text(produto["local"])
                            ]
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Text(produto["data"])
                            ]
                        )
                    ]
                )
            )
            self.tela.tabelaEvento.content.controls.append(linha)

           

    def addEvento(self,e):
        
        e= Evento(
            GeradorID("eventos.json","id").id_gerado,
            self.tela.nomeEvento.value,
            self.tela.local.value,
            self.tela.data.value
        )
        try:
            self.dao.addEventos(e.eventoDict())


            self.tela.nomeEvento.value=""
            self.tela.local.value=""
            self.tela.data.value=""


            self.tela.nomeEvento.update()
            self.tela.local.update()
            self.tela.data.update()
        
            self.listarEventos()

            self.tela.controls=self.tela.layout_inicial
            self.tela.update()

        except Exception as e:
            print(e)






    def voltarTela(self,e):
        self.page.go("/")




