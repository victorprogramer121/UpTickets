from flet import *
import flet as ft
from flet.controls.core import icon



class ViewInicial(View):
    def __init__(self,page:Page):
        super().__init__()
       
        self.route="/inicial"
        self.nomeEvento=TextField(label="Nome Evento",col=4)
        self.local=TextField(label="Local",col=4)
        self.data=TextField(label="dia/mes/ano",col=4)
        self.btnADD=Button("Add",col=3)


        self.tabelaEvento=DataTable(
            columns=[
                
                DataColumn(label=Text("id")),
                DataColumn(label=Text("nomeEvento")),
                DataColumn(label=Text("local")),
                DataColumn(label=Text("data"))
            ],
            col=9
        )


    def build(self):

  
        modalTabela=Container(
            content=self.tabelaEvento,
            
            padding=Padding("20,0,0,10"),
            expand=True
        )
        


        lateral=Container(content=(NavigationRail(
            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=Icons.CREATE,content="Adicionar",
                                         on_click=self.telaADD),
            group_alignment=0.9,
            destinations=[
                NavigationRailDestination(
                    icon=ft.Icons.EXIT_TO_APP,label="Sair"
                )
            ],
            on_change=self.aoMudarDestino
        )
        )

        )
        controles_originais = [
            Row(
                controls=[lateral, VerticalDivider(width=1), modalTabela],
                expand=True
            )
        ]
        self.layout_inicial = controles_originais

        self.controls = controles_originais
        self.controls = controles_originais



        return self.controls
    

    def telaADD(self, e=None):


        add=Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nomeEvento,self.local,self.data
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            self.btnADD
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                    
                ]
                
            )
        )

        self.controls =[
            ResponsiveRow(
                controls=[
                    add
                ]
            )
        ]
        
        
        self.update()


    def aoMudarDestino(self,e):

        if e.control.selected_index==0:
            self.page.go("/")