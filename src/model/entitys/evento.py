from datetime import datetime as dt

class Evento:
    def __init__(self, nomeEvento:str, cidade:str, idadeMIN:int, estado:str,data:dt=None ):
        self.__nomeEvento=nomeEvento
        self.__cidade = cidade
        self.__idadeMIN=idadeMIN
        self.__estado=estado
        self.__data=data

    @property
    def nomeEvento(self)->str:
        return self.__nomeEvento

    @property
    def cidade(self)->str:
        return self.__cidade
    @property
    def idadeMIN(self)->str:
        return self.__idadeMIN
    @property
    def estado(self)->str:
        return self.__estado
    @property
    def data(self)->dt:
        return self.__data


