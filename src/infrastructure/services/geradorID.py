import json
from json import JSONDecodeError
import os

class GeradorID:

    def __init__(self,pastaArquivo,atributo):
        self.pastaArquivo=fr"C:\Users\batis\PycharmProjects\UpTickets\src\infrastructure\database\{pastaArquivo}"
        self.id_gerado=None


        try:
            with open (self.pastaArquivo,"r",encoding="utf-8")as file:
                lista=json.load(file)
                lista_ids=(data[atributo]for data in lista)
                self.id_gerado=max(lista_ids)+1

        except JSONDecodeError as e :
            self.id_gerado=1



if __name__ == '__main__':
    idNovo=GeradorID(r"eventos.json","id").id_gerado
    print(idNovo)
        
