class Fornecedor:
    def __init__(self, nomeFornecedor:str, cnpj:str, senhaFornecedor:str):
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
    def cnpj(self)->str:
        return self.__cnpj

    @cnpj.setter
    def novoCnpj(self, cnpj)->None:
        self.__cnpj=cnpj

    @property
    def senhaFornecedor(self)->str:
        return self.__senhaFornecedor

    @senhaFornecedor.setter
    def novaSenhaFornecedor(self, senhaFornecedor)->None:
        self.__senhaFornecedor=senhaFornecedor