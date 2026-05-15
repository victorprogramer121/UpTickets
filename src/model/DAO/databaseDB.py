import json
from json import JSONDecodeError


class DatabaseDB:
    def __init__(self, pastaArquivo):
        self.__arquivo=fr"src\infrastructure\database\{pastaArquivo}"
        self.__pastaArquivo=pastaArquivo

    def lerArquivo(self)->list:
        try:
            with open(self.__arquivo, "r", encoding="UTF-8") as f:
                return json.load(f)
        except JSONDecodeError:#aqui é um tratamento de erro caso o arquivo não seja um JSON. Ele é tratado aqui mesmo
            return []
        except:
            raise ValueError("Erro ao abrir o arquivo: ", self.__pastaArquivo)#aqui trata o erro, jogando esse erro para ser tratado com outro arquivo

    def salvar(self, dados):
        listaJSON=self.lerArquivo()
        try:
            with open(self.__arquivo, "w", encoding="UTF-8") as f:
                listaJSON.append(dados)
                json.dump(listaJSON, f, ensure_ascii=False, indent=4)
                print("Salvo no JSON!")
        except JSONDecodeError:#aqui é um tratamento de erro caso o arquivo não seja um JSON. Ele é tratado aqui mesmo
            return []
        except:
            raise ValueError("Não foi possível salvar no JSON", self.__pastaArquivo)
        #aqui é uma função que faz com que um novo cadastro vá para o JSON. Caso não encontre o arquivo do JSON, irá dar o erro, que é tratado em outro local

    def historicoCadastro(self, listaCadastros):
        try:
            with open(self.__arquivo, "w", encoding="UTF-8")as f:
                json.dump(listaCadastros, f, ensure_ascii=False, indent=4)
                print("Histórico salvo")
        except:
            raise ValueError("Não foi possível salvar o histórico", self.__pastaArquivo)
    #Salva aquilo que foi deletado