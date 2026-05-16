#TELA LOGIN

from flet import *
import flet as ft
from flet.controls.material import tabs






class ViewLogin(View):
    def __init__(self,page:Page):
        super().__init__(
            )

        page.title="Up Tickets+"

        




        self.email = TextField(label="Email",color="Blue",col=5,icon=ft.Icons.EMAIL)
        self.password=TextField(label="Password",can_reveal_password=False,col=5,color="Blue",password=True,icon=ft.Icons.KEY)
        self.btnEntrarUsuario=Button("Entrar",col=3)
        self.route="/"
        self.bgcolor="Black"
        
        




    def build(self):
        tela_fundo=Container(
                 content=Column(
                      controls=[
                           Image(src="src/view/imagens/party.jpg",border_radius=50,width=200,height=200)
                      ]
                 )
            )

        troca_tela=ft.Tabs(selected_index=0,
                           length=3,
                           expand=True,
                           content=Column(
                               controls=[
                                   TabBar(
                                       tabs=[
                                           Tab(label="Usuario"),
                                       ]
                                   ),
                                   TabBarView(
                                       height=800,
                                       controls=[
                                           Container(
                                               content=Column(
                                                   controls=[
                                                       ResponsiveRow(controls=[
                                                          Image(src="src/view/imagens/party.jpg",border_radius=50,width=200,height=200)
                                                          

                                                       ],
                                                       alignment=MainAxisAlignment.START

                                                           
                                                       ),
                                                       ResponsiveRow(controls=[
                                                            self.email
                                                       ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       ),
                                                       ResponsiveRow(
                                                           controls=[
                                                               self.password
                                                           ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       ),
                                                       ResponsiveRow(controls=[
                                                            self.btnEntrarUsuario
                                                       ],
                                                       alignment=MainAxisAlignment.CENTER
                                                       )
                                                       
                                                   ],

                                               ),
                                               
                                           ),
                                           
                                  
                                       ]


                                   )
                               ]
                           ),

                           )

        self.controls=[
            ResponsiveRow(controls=troca_tela,
            alignment=MainAxisAlignment.SPACE_AROUND,
                          )

        ]
        return self.controls

