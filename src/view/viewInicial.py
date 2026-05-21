from flet import *
import flet as ft
from flet.controls.core import icon
from flet import Tab



class ViewInicial(View):
    def __init__(self,page:Page):
        super().__init__()
       
        self.route="/inicial"
        self.nomeEvento=TextField(label="Nome Evento",col=3,color="Black")
        self.local=TextField(label="Local",col=3,color="Black")
        self.data=TextField(label="dia/mes/ano",col=3,color="Black")
        self.imagem=Image(src="src/view/imagens/party.jpg",width=200,height=200)
        self.btnADD=Button("Add",col=2)
        self.bgcolor="Black"
        
        
        
        
        


        self.tabelaEvento=Container(
            bgcolor="White",
            content=Column(
                controls=[
                    
                ],
                scroll=ft.ScrollMode.ALWAYS
                
            ),
            expand=True
        )


    

                


    def build(self):



          
        self.modalTabela = Container(
            content=self.tabelaEvento,
            padding=ft.Padding(left=20, top=10, right=10, bottom=10), 
            expand=False
        )
        
        self.hub=Container(
            expand=True,
            width=2350,
            height=1450,
            bgcolor=ft.Colors.WHITE,
            content=Column(
                controls=[
                   self.modalTabela
                ]
            )
        

        )
        
        self.telaCadastro=Container(
            width=2350,
            height=1450,
            bgcolor=ft.Colors.WHITE,
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
                    Divider(height=5, color=ft.Colors.BLACK_26),
                    NavigationRail(
                        selected_index=2,
                        label_type=NavigationRailLabelType.ALL,
                        bgcolor=ft.Colors.BLUE_GREY,
                        extended=True,
                        height=1400,
                        on_change=self.mudarConteudo,
                        destinations=[

                            ft.NavigationRailDestination(
                                label="Menu",
                                icon=ft.Icons.HOME,
                                selected_icon=ft.Icons.HOME,
                               
                            ),
                            
                            ft.NavigationRailDestination(
                                label="Adicionar",
                                icon=ft.Icons.ADD,
                                selected_icon=ft.Icons.ADD,
                                
                            
                                
                            ),
                            
                            
                            
                            ft.NavigationRailDestination(
                                label="Sair",
                                icon=ft.Icons.EXIT_TO_APP,
                                selected_icon=ft.Icons.EXIT_TO_APP,
                               
                                
                                

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

                            
                            Image(src="src/view/imagens/logo.png",width=150,height=100,),
                            Text("Up Tickets",color=ft.Colors.WHITE,text_align=TextAlign.END,size=30,)
                            
                            
                            
                        ],
                        alignment=MainAxisAlignment.START,
                        
                        
                    ),
                    
                ]
            )
        )

       

        









        self.controls=[
            ResponsiveRow(
                controls=[
                    telaInicial,
                    Row(
                        controls=[
                            lateral,self.hub,
                        ]
                    )
                ],
                alignment=MainAxisAlignment.CENTER
            )
        ]

    def mudarConteudo(self, e):
            indiceSelecionado=e.control.selected_index

            if indiceSelecionado == 0:
                self.hub.content = Column(
                     controls=[
                          self.modalTabela
                     ]
                    )
                
                print("tela mudando para o menu")

            elif indiceSelecionado == 1:
                self.hub.content = Column(
                     controls=[
                          self.telaCadastro
                     ]
                )
                

                print("tela mudando para cadastro")

            elif indiceSelecionado == 2:
                self.page.go("/")
                print("tela mudando para login")

            self.update()





  
     


        