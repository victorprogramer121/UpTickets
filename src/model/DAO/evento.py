from src.model.DAO.databaseDB import DatabaseDB


class Eventos_DAO:

    def __init__(self):
        self.__conn = DatabaseDB("eventos.json")

    def addEventos(self, dados:dict):
        try:
            self.__conn.salvar(dados)
            return "Evento criado com sucesso"
        except Exception as e:
            raise ValueError("Não foi possivel criar o evento",e)

    def visualizarEvento(self):
        try:
            return self.__conn.lerArquivo()
        except Exception as e:
            raise ValueError("erro ao ler evento",e)



    def deletarEvento(self,id):

            novaLista=[evento for evento in self.visualizarEvento() if evento["id"]!=id]
            if len(novaLista)==len(self.visualizarEvento()):
                 raise ValueError("Nenhum produto encontrado com esse ID")
            self.__conn.historicoCadastro(novaLista)
            print("deletado com sucesso")

if __name__ == '__main__':
    e1=Eventos_DAO()
    # dados={"id":1,
    # "nomeEvento":"kle",
    # "local":"rua",
    # "idadeMIN":16,
    # "data":160411
    #        }
    # e1.addEventos(dados)
    try:
        e1.deletarEvento(1)
    except Exception as e:
         print("erro",e)




