from abc import ABC, abstractmethod




class UsuarioIfro(ABC):




    def __init__(self, nome, idade,login_usuario,login_senha):
            self.nome = nome
            self.idade = idade
            self._login_usuario = login_usuario
            self._login_senha = login_senha




    def get_nome (self):
        return self.nome




    def set_nome(self,nome):
        self.nome = nome




    def get_idade(self):
        return self.idade




    def set_idade (self, idade):
        self.idade = idade




    def get_login_usuario(self):
        return self._login_usuario




    def set_login_usuario(self, novo_login):
        self._login_usuario = novo_login




    def get_login_senha(self):
        return self._login_senha




    def set_login_senha(self,nova_senha):
        self._login_senha = nova_senha




    @abstractmethod




    def cadastrar ():
        pass
