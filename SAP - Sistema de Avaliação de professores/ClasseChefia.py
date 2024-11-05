from ClasseUsuario import*
from random import *


class ChefiaImediata(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, idChefia, email):
        super().__init__(nome, idade, login_usuario,login_senha)
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
        pass


    def reprovarAvaliacao(self):
        pass


    def cadastrar(self):
     self.nome = input("Digite seu nome: ")
     self.idade = int(input("Digite sua idade:"))
     self._login_usuario = input("Cadastre um usuário: ")
     self._login_senha = input("Cadastre uma senha: ")
     self.idChefia = print(randint(100, 300))
     self.disciplina_ministrada = input("Digite seu email: ")
