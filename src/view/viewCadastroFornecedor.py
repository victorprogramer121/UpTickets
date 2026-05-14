#TELA CADASTRO FORNECEDOR

from certifi import contents
from flet import *
import flet as ft
from flet.controls.core import column
from flet.controls.material import container


class ViewCadastroFornecedor(View):
    def __init__(self, page: Page):
        super().__init__(
            route="/cadastroFornecedor")

        page.title = "Up Tickets+"

        self.nome = TextField(label="Nome", col=5,color="Black")
        self.cadastrarPassword = TextField(label="Password", col=5,color="White")
        self.cnpj = TextField(label="CNPJ", col=5,color="White")
        self.btnCadastro = Button("Cadastrar", col=3, color="Blue",icon=ft.Icons.LOGIN)


    def build(self):
        modalCadastro =Container(
            content=Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            self.nome
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            self.cnpj
                        ],
                        alignment=MainAxisAlignment.CENTER,

                    ),
                    ResponsiveRow(
                        controls=[
                            self.cadastrarPassword
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            self.btnCadastro
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                ]

            )
        )
        self.controls=[
            ResponsiveRow(
                controls=[
                    modalCadastro
                ]
            )
        ]
        return self.controls