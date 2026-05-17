from flet import *
import flet as ft
from flet.controls.core import icon
from flet import Tab



class ViewInicial(View):
    def __init__(self,page:Page):
        super().__init__()
       
        self.route="/inicial"
        self.nomeEvento=TextField(label="Nome Evento",col=4)
        self.local=TextField(label="Local",col=4)
        self.data=TextField(label="dia/mes/ano",col=4)
        self.btnADD=Button("Add",col=3)
        self.bgcolor="Black"
        
        
        
        


        self.tabelaEvento=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            Image(src="src/view/imagens/party.jpg",width=200,height=200)
                        ]
                    ),
                    ResponsiveRow(
                        controls=[
                            Text("id")
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Image(src="src/view/imagens/party.jpg")
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Text("Nome Evento")
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Text("local")
                        ]
                    ),
                    ResponsiveRow(
                        controls=[
                            Text("data")
                        ]
                    )
                ]
                
            )
        )


    def build(self):



          
        modalTabela=Container(
            content=self.tabelaEvento,
            
            padding=Padding("20,10,10,10"),
            expand=True



        
            
            
            
        )
        lateral=Container(
            width=200,
            bgcolor=ft.Colors.BLUE_900,
            content=Column(
                tight=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Text("MENU",size=20)
                        ]
                    ),
                    Divider(height=1, color=ft.Colors.BLACK_26),
                    NavigationRail(
                        selected_index=1,
                        label_type=NavigationRailLabelType.ALL,
                        bgcolor=ft.Colors.BLUE_GREY,
                        extended=True,
                        height=1400,
                        destinations=[
                            ft.NavigationBarDestination(
                                label="Adicionar",
                                icon=ft.Icons.ADD,
                                selected_icon=ft.Icons.ADD
                                
                            ),
                            
                            
                            ft.NavigationBarDestination(
                                label="Sair",
                                icon=ft.Icons.EXIT_TO_APP,
                                selected_icon=ft.Icons.EXIT_TO_APP
                            )
                        ]
                    )
                ]
            )
        )


        telaInicial=Container(
            width=200,
            height=100,
            expand=True,
            bgcolor=ft.Colors.BLUE_900,
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Text("UpTickets",color=ft.Colors.BLACK,size=20)
                        ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            )
        )
        self.controls=[
            ResponsiveRow(
                controls=[
                    telaInicial,
                    Row(
                        controls=[
                            lateral
                        ]
                    )
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]
        





  
     


        