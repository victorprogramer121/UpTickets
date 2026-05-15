import json
from json import JSONDecodeError
import os

class GeradorID:

    def __init__(self,pastaArquivo,atributo):
        self.pastaArquivo=fr"src\infrastructure\database\{pastaArquivo}"
        self.id_gerado=None


        try:
            with open (self.pastaArquivo,"r",encoding="utf-8")as file:
                lista=json.load(file)
                if not lista:
                    self.id_gerado=1
                else:
                    lista_ids=(dados[atributo] for dados in lista)
                    self.id_gerado=max(lista_ids)+1

        except (FileNotFoundError,json.JSONDecodeError) :
            self.id_gerado=1
        





        
