#TELA LOGIN

from flet import *
import flet as ft
from flet.controls.material import tabs






class ViewLogin(View):
    def __init__(self,page:Page):
        super().__init__(
            route="/")

        page.title="Up Tickets+"
        page.ft.bgcolor="White"




        self.email = TextField(label="Email",color="Black",col=5 )
        self.password=TextField(label="Password",can_reveal_password=False,col=5,color="Black")
        self.cnpj=TextField(label="CNPJ",col=5,color="Black")
        self.btnEntrar=Button("Entrar",col=3)
        self.cadastro=Text("é seu primeiro acesso? Clique para se cadastrar")




    def build(self):
        troca_tela=ft.Tabs(selected_index=1,
                           length=3,
                           expand=True,
                           content=Column(
                               controls=[
                                   TabBar(
                                       tabs=[
                                           Tab(label="Usuario"),
                                           Tab(label="Fornecedor")
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
                                                               self.btnEntrar
                                                           ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       )
                                                   ],

                                               )
                                           ),
                                           Container(
                                               content=Column(
                                                   controls=[
                                                       ResponsiveRow(
                                                           controls=[
                                                               self.cnpj
                                                           ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       ),
                                                        ResponsiveRow(
                                                            controls=[
                                                                self.password
                                                            ],
                                                            alignment=MainAxisAlignment.CENTER
                                                        ),
                                                       ResponsiveRow(
                                                           controls=[
                                                               self.btnEntrar
                                                           ],
                                                           alignment=MainAxisAlignment.CENTER
                                                       )
                                                   ]
                                               )
                                           )
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

