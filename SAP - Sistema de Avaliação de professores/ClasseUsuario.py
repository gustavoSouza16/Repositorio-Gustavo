from abc import ABC, abstractmethod

class UsuarioIfro(ABC):
    def __init__(self, nome, idade,login_usuario,login_senha):
            self.__nome = nome
            self.__idade = idade
            self.__login_usuario = login_usuario
            self.__login_senha = login_senha

    def get_nome (self):
        return self.__nome
        
    def set_nome(self,nome):
        self.__nome = nome
        
    def get_idade(self):
        return self.__idade
        
    def set_idade (self, idade):
        self.__idade = idade
        
    def get_login_usuario(self):
        return self.__login_usuario
        
    def set_login_usuario(self, novo_login):
        self.__login_usuario = novo_login
        
    def get_login_senha(self):
        return self.__login_senha
        
    def set_login_senha(self,nova_senha):
        self.__login_senha = nova_senha

    @abstractmethod
    
    def cadastrar ():
        pass