class Usuario:
    def __init__(self, email:str, senhaUsuario:str):
        # self.__nomeUsuario=nomeUsuario
        self.__email=email
        self.__senhaUsuario = senhaUsuario

    # @property
    # def nomeUsuario(self)->str:
    #     return self.__nomeUsuario

    # @nomeUsuario.setter
    # def novoNomeUsuario(self, nomeUsuario)->None:
    #     self.__nomeUsuario=nomeUsuario

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def novoEmail(self, email) -> None:
        self.__email = email

    @property
    def senhaUsuario(self)->str:
        return self.__senhaUsuario

    @senhaUsuario.setter
    def novaSenhaUsuario(self, senhaUsuario)->None:
        self.__senhaUsuario=senhaUsuario

    #Tem que tratar a senha para ficar com a máscara


    def __eq__(self, other):#função de comparação pra verificar se já existe esse email no cadatro de usuário
        return self.__email==other.email, print(f"O email já está cadastrado")
    #verificar se está certo

    def usuario(self)->dict:
        return {
            "email":self.__email,
            "senha":self.__senhaUsuario
        }

