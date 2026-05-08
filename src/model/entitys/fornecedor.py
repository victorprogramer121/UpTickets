class Fornecedor:
    def __init__(self, nomeFornecedor:str, senhaFornecedor:str, cnpj:str):
        self.__nomeFornecedor=nomeFornecedor
        self.__cnpj=cnpj
        self.__senhaFornecedor=senhaFornecedor

    @property
    def nomeFornecedor(self)->str:
        return self.__nomeFornecedor

    @nomeFornecedor.setter
    def novoNomeFornecedor(self, nomeFornecedor)->None:
        self.__nomeFornecedor=nomeFornecedor

    @property
    def senhaFornecedor(self) -> str:
        return self.__senhaFornecedor

    @senhaFornecedor.setter
    def novaSenhaFornecedor(self, senhaFornecedor) -> None:
        self.__senhaFornecedor = senhaFornecedor

    @property
    def cnpj(self)->str:
        return self.__cnpj

    @cnpj.setter
    def novoCnpj(self, cnpj)->None:
        self.__cnpj=cnpj

    def __eq__(self, other):
        return self.__cnpj==other.__cnpj, print(f"O cnpj informado já está cadastrado")
    #verificar se está correto

    def fornecedor(self)->dict:
        return {
            "nome":self.__nomeFornecedor,
            "senha":self.__senhaFornecedor,
            "cnpj": self.__cnpj
        }