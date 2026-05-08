from datetime import datetime as dt

class Evento:
    def __init__(self, nomeEvento:str, local:str, idadeMIN:int, estado:str,data:dt=None ):
        # self.__cpf=cpf
        self.__nomeEvento=nomeEvento
        self.__local = local
        self.__idadeMIN=idadeMIN
        self.__estado=estado
        self.__data=data

    # @property
    # def cpf(self)->str:
    #     return self.__cpf

    @property
    def nomeEvento(self)->str:
        return self.__nomeEvento

    @property
    def local(self)->str:
        return self.__cidade
    @property
    def idadeMIN(self)->str:
        return self.__idadeMIN
    @property
    def data(self)->dt:
        return self.__data

    def __eq__(self, other):
        return self.__nomeEvento==other.__nomeEvento and self.__local==other.__local, print("Evento duplicado")
    #verificar se está correto

    def evento(self)->dict:
        return {
            "nomeEvento":self.__nomeEvento,
            "local":self.__local,
            "idadeMIN":self.__idadeMIN,
            "data":self.__data
        }


