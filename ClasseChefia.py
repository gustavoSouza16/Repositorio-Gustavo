from ClasseAluno import*
from ClasseProfessor import*
from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseAvaliacao import *
from random import *

class ChefiaImediata(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, idChefia, email):
        super().__init__(nome, idade, login_senha, login_usuario)
        self.idChefia = idChefia
        self.email = email
        self.Avaliacao = None

    def get_idChefia(self):
        return self.idChefia

    def get_email(self):
        return self.email

    def set_idChefia(self, novoID):
        self.idChefia = novoID

    def set_email(self, novoEmail):
        self.email = novoEmail

    def aprovarAvaliacao(self, Avaliacao):
        return Avaliacao, print("Avaliação Aprovada, Parabéns!")

    def reprovarAvaliacao(self):
        pass

    def cadastrar(self):
        self.nome = input("Digite seu nome: ")
        self.idade = int(input("Digite sua idade:"))
        self._login_usuario = input("Cadastre um usuário: ")
        self._login_senha = input("Cadastre uma senha: ")
        self.idChefia = print(randint(100, 300))
        self.disciplina_ministrada = input("Digite seu email: ")
