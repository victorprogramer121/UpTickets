from src.view.viewLogin import ViewLogin
from src.controllers.produtoController import ViewController

def produtoConstructor(page):
    loginView=ViewLogin(page)
    controlador=ViewController(page,loginView)



    return loginView