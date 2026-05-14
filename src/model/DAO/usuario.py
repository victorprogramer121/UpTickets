from src.model.DAO.databaseDB import DatabaseDB


class UsuarioDAO:

    def __init__(self):
        self.__conn=DatabaseDB("usuarios.json")


    def addUsuario(self,dados:dict):
        try:
            self.__conn.salvar(dados)
            return f"usuario salvo com sucesso"
        except Exception as e:
            raise ValueError("erro na hora de salva fdp desgracado, salva essa porra de novo, jumento",e)


    def deletarUsuario(self,nomeUsuario):
        novoUsuario=[usuario for usuario in self.lerUsuario() if usuario["email"]!=nomeUsuario]
        if len(novoUsuario)==len(self.lerUsuario()):
            raise ValueError("nenhum usuario encontrado")
        self.__conn.historicoCadastro(novoUsuario)
        print("deletado com sucesso")


    def lerUsuario(self):
        return self.__conn.lerArquivo()