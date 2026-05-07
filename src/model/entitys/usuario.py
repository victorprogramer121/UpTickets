class Usuario:
    def __init__(self, nomeUsuario:str, senhaUsuario:str, email:str):
        self.__nomeUsuario=nomeUsuario
        self.__senhaUsuario=senhaUsuario
        self.__email=email

    @property
    def nomeUsuario(self)->str:
        return self.__nomeUsuario

    @nomeUsuario.setter
    def novoNomeUsuario(self, nomeUsuario)->None:
        self.__nomeUsuario=nomeUsuario

    @property
    def senhaUsuario(self)->str:
        return self.__senhaUsuario

    @senhaUsuario.setter
    def novaSenhaUsuario(self, senhaUsuario)->None:
        self.__senhaUsuario=senhaUsuario

    @property
    def email(self)->str:
        return self.__email

    @email.setter
    def novoEmail(self, email)->None:
        self.__email=email