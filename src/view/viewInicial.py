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


        telaInicial=ft.Tabs(
            selected_index=1,
            length=3,
            expand=3,
            content=Column(
                controls=[
                    TabBar(
                        tabs=[
                            Tab(label="Usuario")
                        ]
                    ),
                    TabBarView(
                        height=300,
                        controls=[
                            Container(
                                content=Column(
                                    controls=[
                                        modalTabela
                                    ],
                                    alignment=MainAxisAlignment.CENTER
                                )
                            )
                        ]
                    )
                ]
            )
        )
        self.controls=[
            ResponsiveRow(
                controls=[
                    telaInicial
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]
        





  
     


        