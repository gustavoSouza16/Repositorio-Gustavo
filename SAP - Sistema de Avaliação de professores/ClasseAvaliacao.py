from random import *
from datetime import *

class Avaliacao:
    def __init__(self, idAvaliacao, conteudoAvaliacao, dataehoraAvaliacao, remetenteAvaliacao, destinatarioAvaliacao):
        self.idAvaliacao = idAvaliacao
        self.conteudoAvaliacao = conteudoAvaliacao
        self.dataehoraAvaliacao = dataehoraAvaliacao
        self.remetenteAvaliacao = remetenteAvaliacao
        self.destinatarioAvaliacao = destinatarioAvaliacao
        self.respostaAvaliacao = None

    def get_idAvaliacao(self):
        return self.idAvaliacao

    def get_conteudoAvaliacao(self):
        return self.idAvaliacao

    def get_dataAvaliacao(self):
        return self.dataAvaliacao

    def get_horaAvaliacao(self):
        return self.horaAvaliacao

    def get_remetenteAvaliacao(self):
        return self.remetenteAvaliacao.get_nome()

    def get_destinatarioAvaliacao(self):
        return self.destinatarioAvaliacao

    def get_respostaAvaliacao(self):
        return self.respostaAvaliacao

    def set_idAvaliacao(self, idAvaliacao):
        self.idAvaliacao = idAvaliacao

    def set_conteudoAvaliacao(self, conteudoAvaliacao):
        self.conteudoAvaliacao = conteudoAvaliacao

    def set_dataAvaliacao(self, dataAvaliacao):
        self.dataAvaliacao = dataAvaliacao

    def set_horaAvaliacao(self, horaAvaliacao):
        self.horaAvaliacao = horaAvaliacao

    def set_remetenteAvaliacao(self, remetenteAvaliacao):
        self.remetenteAvaliacao = remetenteAvaliacao

    def set_destinatarioAvaliacao(self, destinatarioAvaliacao):
        self.destinatarioAvaliacao = destinatarioAvaliacao

    def set_respostaAvaliacao(self, respostaAvaliacao):
        self.respostaAvaliacao = respostaAvaliacao


    def gerarAvaliacao(self):
        data = datetime.date
        Hora = datetime.hour
        self.idAvaliacao = randint(100, 300)
        self.conteudoAvaliacao = len(input("(Limite de 300 palavras!)\nFaça sua avaliação para o docente desejado:\n-"))
        self.dataehoraAvaliacao = print(f"Dia: {data}\n Hora:{Hora}")
        self.remetenteAvaliacao = input("Por Favor Digite seu nome Completo:\n-")
        self.destinatarioAvaliacao = input("Digite o nome do professor Destinatário:\n-")

    def consultarStatus(self):
        pass
