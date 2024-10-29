from ClasseAluno import*
from ClasseProfessor import*
from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseAvaliacao import *

class ChefiaImediata(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, idChefia, email):
        super().__init__(self, nome, idade, login_senha, login_usuario)
        self.idChefia = idChefia
        self.email = email
        self.Avaliacao = Avaliacao
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