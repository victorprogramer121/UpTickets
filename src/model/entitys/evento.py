from datetime import datetime as dt
from src.infrastructure.services.geradorID import GeradorID


class Evento:
    def __init__(self,id: int, imagem,nomeEvento: str, local:  int,data: dt = None):
        # self.__cpf=cpf
        self.__nomeEvento = nomeEvento
        self.__local = local
        self.__imagem=imagem
        self.__data = data
        self.__id =id


    @property
    def imagem(self):
        return self.__imagem

    @property
    def nomeEvento(self) -> str:
        return self.__nomeEvento

    @property
    def data(self) -> dt:
        return self.__data
    
    @property
    def id(self)->int:
        return self.__id
    

    def __eq__(self, other):
        return self.__nomeEvento == other.__nomeEvento and self.__local == other.__local, print("Evento duplicado")

    # verificar se está correto

    def eventoDict(self) -> dict:
        return {
            "id":self.__id,
            "imagem":self.__imagem,
            "nomeEvento":self.__nomeEvento,
            "local":self.__local,
            "data":self.__data
            
        }
    @staticmethod
    def dict_to_obejct(dados):
        return Evento(
            dados["id"],
            dados["imagem"],
            dados["nomeEvento"],
            dados["local"],
            dados["data"]
        )

