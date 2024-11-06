class Avaliacao:
    def __init__(self, idAvaliacao, conteudoAvaliacao, dataehoraAvaliacao, remetenteAvaliacao, destinatarioAvaliacao):
        self.idAvaliacao = idAvaliacao
        self.conteudoAvaliacao = conteudoAvaliacao
        self.dataehoraAvaliacao = dataehoraAvaliacao
        self.remetenteAvaliacao = remetenteAvaliacao
        self.destinatarioAvaliacao = destinatarioAvaliacao
        self.status = None
        self.respostaAvaliacao = None
        
    def get_idAvaliacao(self):  
        return f"\n\n\ID da avaliação: {self.idAvaliacao}\n\n"
        
    def get_conteudoAvaliacao(self):    
        return self.conteudoAvaliacao
        
    def get_dataehoraAvaliacao(self):
        return self.dataehoraAvaliacao

    def get_remetenteAvaliacao(self):
        return f"\n\nRemetente da avaliação: {self.remetenteAvaliacao.get_nome()}\nAno escolar do Remetente: {self.remetenteAvaliacao.get_ano_escolar()}\nCurso do Remetente: {self.remetenteAvaliacao.get_curso()}"

    def get_destinatarioAvaliacao(self):
        return f"\n\nDestinatário da avaliação: {self.destinatarioAvaliacao.get_nome()}\nDisciplina ministrada pelo Destinatário: {self.destinatarioAvaliacao.get_disciplina_ministrada()}"
    
    def get_respostaAvaliacao(self):
        if self.respostaAvaliacao == None:
            return "\n\nResposta do Destinatário:\nA avaliação ainda não foi respondida pelo Destinatário\n\n"
        else:    
            return f"\n\nResposta do Destinatário:\n{self.respostaAvaliacao}\n\n"
    
    def set_idAvaliacao(self, idAvaliacao):
        self.idAvaliacao = idAvaliacao

    def set_conteudoAvaliacao(self, conteudoAvaliacao):
        self.conteudoAvaliacao = conteudoAvaliacao

    def set_horaAvaliacao(self, horaAvaliacao):
        self.horaAvaliacao = horaAvaliacao

    def set_remetenteAvaliacao(self, remetenteAvaliacao):
        self.remetenteAvaliacao = remetenteAvaliacao

    def set_destinatarioAvaliacao(self, destinatarioAvaliacao):
        self.destinatarioAvaliacao = destinatarioAvaliacao

    def set_respostaAvaliacao(self, respostaAvaliacao):
        self.respostaAvaliacao = respostaAvaliacao

    def gerarAvaliacao(self):
        return (f"{self.get_idAvaliacao()}{self.get_remetenteAvaliacao()}{self.get_destinatarioAvaliacao()}{self.get_respostaAvaliacao()}")

    def consultarStatus(self):
        if self.status == None:
            print ("A avaliação ainda não foi revisado.\nStatus: Em Andamento")
        else:
            print (f"Status da avaliação: {self.status}")
