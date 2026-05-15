#TELA LOGIN

from flet import *
import flet as ft
from flet.controls.material import tabs






class ViewLogin(View):
    def __init__(self,page:Page):
        super().__init__(
            )

        page.title="Up Tickets+"

        




        self.email = TextField(label="Email",color="Black",col=5 )
        self.password=TextField(label="Password",can_reveal_password=True,col=5,color="Black")
        self.btnEntrarUsuario=Button("Entrar",col=3)
        self.route="/"




    def build(self):
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
                                       height=300,
                                       controls=[
                                           Container(
                                               content=Column(
                                                   controls=[
                                                       ResponsiveRow(controls=[
                                                           self.email

                                                       ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       ),
                                                       ResponsiveRow(controls=[
                                                            self.password
                                                       ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       ),
                                                       ResponsiveRow(
                                                           controls=[
                                                               self.btnEntrarUsuario
                                                           ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       )
                                                   ],

                                               )
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

