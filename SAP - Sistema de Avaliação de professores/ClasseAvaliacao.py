class Avaliacao:
    def __init__(self, conteudoAvaliacao, dataehoraAvaliacao, remetenteAvaliacao, destinatarioAvaliacao):
        self.__idAvaliacao = None
        self.__conteudoAvaliacao = conteudoAvaliacao
        self.__dataehoraAvaliacao = dataehoraAvaliacao                                                      
        self.__remetenteAvaliacao = remetenteAvaliacao                                                  #Associação
        self.__destinatarioAvaliacao = destinatarioAvaliacao                                            #Associação
        self.__status = None

    def get_idAvaliacao(self):  
        return f"\n\nID da avaliação: {self.__idAvaliacao}\n\n"
        
    def get_conteudoAvaliacao(self):    
        return self.__conteudoAvaliacao
        
    def get_dataehoraAvaliacao(self):
        return self.__dataehoraAvaliacao

    def get_remetenteAvaliacao(self):
        return f"\n\nRemetente da avaliação: {self.__remetenteAvaliacao.get_nome()}\nAno escolar do Remetente: {self.__remetenteAvaliacao.get_ano_escolar()}\nCurso do Remetente: {self.__remetenteAvaliacao.get_curso()}"

    def get_destinatarioAvaliacao(self):
        return f"\n\nDestinatário da avaliação: {self.__destinatarioAvaliacao.get_nome()}\nDisciplina ministrada pelo Destinatário: {self.__destinatarioAvaliacao.get_disciplina_ministrada()}"
    
    def set_idAvaliacao(self, idAvaliacao):
        self.__idAvaliacao = idAvaliacao

    def set_conteudoAvaliacao(self, conteudoAvaliacao):
        self.__conteudoAvaliacao = conteudoAvaliacao

    def set_dataehoraAvaliacao(self, dataehoraAvaliacao):
        self.__dataehoraAvaliacao = dataehoraAvaliacao

    def set_remetenteAvaliacao(self, remetenteAvaliacao):
        self.__remetenteAvaliacao = remetenteAvaliacao

    def set_destinatarioAvaliacao(self, destinatarioAvaliacao):
        self.__destinatarioAvaliacao = destinatarioAvaliacao

    def gerarAvaliacao(self):
        return (f"{self.__get_idAvaliacao()}{self.__get_remetenteAvaliacao()}{self.__get_destinatarioAvaliacao()}{self.__get_respostaAvaliacao()}")

    def consultarStatus(self):
        if self.__status == None:
            print ("A avaliação ainda não foi revisado.\nStatus: Em Andamento")
        else:
            print (f"Status da avaliação: {self.__status}")

