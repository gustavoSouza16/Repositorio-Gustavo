from random import *
from datetime import *

listaNum = []

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
        data = datetime.date #Data e Hora ao vivo
        Hora = datetime.hour
        self.idAvaliacao = randint(100, 300) #Gera um número aleatório para o id
        listaNum.append(self.idAvaliacao) #Adiciona esse numero na lista
        print(f"Seu id é: {self.idAvaliacao}")
        if self.idAvaliacao in listaNum: #Se ja tiver na lista o programa refaz o id (esperokk)
            self.idAvaliacao = randint(100, 300)
            return print(f"Seu id é: {self.idAvaliacao}")
            listaNum.append(self.idAvaliacao) # Adiciona o novo id na lista || ou usar o set_idAvaliacao kk
        self.conteudoAvaliacao = input("(Limite de 300 palavras!)\nFaça sua avaliação para o docente desejado:\n-").strip #Limite pra n extrapolar a quanitdade de caracteres
        if len(self.conteudoAvaliacao) > 300:
            print("Excedeu o limite máximo de caracteres, por favor refaça!")
        self.dataehoraAvaliacao = print(f"Dia: {data}\n Hora:{Hora}") #Data e hora em que você criou o objeto
        self.remetenteAvaliacao = input("Por Favor Digite seu nome Completo:\n-") #Seu nome né
        self.destinatarioAvaliacao = input("Digite o nome do professor Destinatário:\n-") #O prof destinatario || sera q é bom fazer uma lista de prof?

    def consultarStatus(self):
        pass
