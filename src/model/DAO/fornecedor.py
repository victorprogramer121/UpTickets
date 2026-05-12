
from src.model.DAO.databaseDB import DatabaseDB

class FornecedorDAO:
    def __init__(self):
        self.__conn=DatabaseDB("fornecedores.json")

    def addFornecedor(self, dados:dict):
        try:
            self.__conn.salvar(dados)
            return f"Fornecedor salvo com sucesso"
        except Exception as e:
            raise ValueError("Erro ao salvar o fornecedor", e)
        #Aqui faz a tratativa de erro, caso não salve o fornecedor na lista de fornecedores do banco de dados
    def lerFornecedor(self):
        try:
            return self.__conn.lerArquivo()
        except Exception as e:
            raise ValueError("Erro ao ler fornecedor",e)
        #Tratativa de erro caso não tenha nenhum fornecedor na lista


    def deletarFornecedor(self, nomeFornecedor):
        novoFornecedor=[fornecedor for fornecedor in self.lerFornecedor() if fornecedor["nomeFornecedor"]!=nomeFornecedor]
        if len(novoFornecedor)==len(self.lerFornecedor()):
            raise ValueError("Não existe nenhum cadastro desse fornecedor em nosso banco de dados")

        self.__conn.historicoCadastro(novoFornecedor)
        print(f"Deletado com sucesso")
        #aqui ele salva depois que deleta para atualizar o banco de dados

if __name__ == '__main__':
    f1=FornecedorDAO()
    # dados={'nomeFornecedor':'Leonardo LTDA', 'senhaFornecedor':'vitin0909', 'cpnj':'76867559757513'}
    # m=f1.addFornecedor(dados)
    # print(m)
    # primeiro código para inserir fornecedores dentro do banco de dados

    try:
        f1.deletarFornecedor("Leonardo LTDA")
    except Exception as e:
        print("Erro:", e)
