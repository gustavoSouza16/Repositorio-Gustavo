class Mural:
    def __init__(self):
        self.__idMural = None
        self.__descricao = "O mural é o local onde o usuário pode inserir suas avaliações feitas para um docente de sua instituição e ver outras avaliações realizadas por outros discentes."                                                                     
        self.__avaliacoesAprovados = []                                                             #Agregação
    
    def get_idMural(self):
        return self.__idMural
    
    def get_descricao(self):
        return self.__descricao
    
    def set_idMural(self, novoID):
        self.__idMural = novoID
    
    def set_descricao(self,nova_descricao):
        self.__descricao = nova_descricao
    
    def adicionarAvaliacao(self, Avaliacao):
        self.__avaliacoesAprovados.append(Avaliacao)
        
    def consultarAvaliacao(self):       #Utilização dos comandos de tratamento  de exceção
        try:
            if not self.__avaliacoesAprovados:
                raise ValueError('Não há avaliações disponíveis no mural.')
            print("-"*100)
            for avaliacao in self.__avaliacoesAprovados:
                print (avaliacao.get_idAvaliacao(),
                       avaliacao.get_conteudoAvaliacao(),
                       avaliacao.get_remetenteAvaliacao(),
                         avaliacao.get_destinatarioAvaliacao(),
                           avaliacao.get_respostaAvaliacao())
            print("-"*100)
        
        except ValueError:
            print('Não há avaliações disponíveis no mural.')
        except Exception:
            print('Ocorreu um erro inesperado.')
        finally:
            print('Consulta no mural finalizada.')




