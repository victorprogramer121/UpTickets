from flet import *
import flet as ft
from flet.controls.core import icon
from flet.controls.material import bottom_app_bar


class ViewInicial(View):
    def __init__(self,page:Page):
        super().__init__()
       
        self.route="/inicial"


    def build(self):

        caixa=Container(
            expand=True,
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            Image(src=fr"C:\Users\klebe\PycharmProjects\SistemadeVendas\asc\view\party.jpg")
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Text("Evento",text_align=TextAlign.JUSTIFY,size=20,color="red",weight=FontWeight.BOLD)
                        ]
                    ),
                    ResponsiveRow(
                        controls=[
                            TextButton("Comprar",col=4),
                            Icon(icon=CupertinoIcons.HEART,col=4),

                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )
                ],
                col={ResponsiveRowBreakpoint.XS:12,
                     ResponsiveRowBreakpoint.LG:4}
            )
        )


        lateral=Container(content=(NavigationRail(
            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=Icons.CREATE,content="Adicionar"),
            group_alignment=0.9,
            destinations=[
                NavigationRailDestination(
                    icon=ft.Icons.EXIT_TO_APP,label="Sair"
                )
            ],
        )
        )

        )

        self.controls=[
           Row(
                controls=[
                    lateral,
                    VerticalDivider(width=1),
                    caixa
                ],
                expand=True
            )
        ]


        return self.controls
        
        