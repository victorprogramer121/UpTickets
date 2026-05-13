from flet import *



class TelaInicial(View):
    def __init__(self,page:Page):
        super().__init__(
            route="/inicial"
        )

        page.title = "Up Tickets"

        
        