from src.model.DAO.databaseDB import DatabaseDB



class Eventos_DAO:


    def __init__(self):
            self.__conn=DatabaseDB("eventos.json")



    def addEventos(self,data=dict):
          try:
                self.__conn.salvar(data)
                return "Evento criado com sucesso"
          except Exception as e:
                raise ValueError("Não foi possivel criar o evento")
          
    def visualizarEvento(self):
          return self.__conn.lerArquivo
    

    