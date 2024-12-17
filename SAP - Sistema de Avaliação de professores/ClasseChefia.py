from ClasseUsuario import*
from random import *

class ChefiaImediata(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, email):
        super().__init__(nome, idade, login_usuario,login_senha)
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, novoEmail):
        self.__email = novoEmail

    def visualizarAvaliacao(self,avaliacao):
        return avaliacao.gerarAvaliacao()                                                                 #Relacionamento de Associação

    def aprovarAvaliacao(self, mural,avaliacao):
        print("Avaliação aprovada e sendo inserida no Mural")
        mural.adicionarAvaliacao(avaliacao)                                                               #Relacionamento de Agregação
        print ("Avaliação inserida e disponível para os professores destinatários vizualizarem")
        
    def reprovarAvaliacao(self):
        print ("A Avaliação foi reprovada.")

    def cadastrar(self):
        while True:
            nome = input("Digite seu nome: ")
            self.set_nome(nome)
            try: 
                idade = int(input("Digite sua idade:"))
            except:
                print("Coloque a idade utilizando números")
                continue
                                    
            self.set_idade(idade)
            login_usuario = input("Cadastre um usuário: ")
            self.set_login_usuario(login_usuario)
            login_senha = input("Cadastre uma senha: ")                                #Acrescentar um raise que, caso a senha seja menor que 8 caracteres, vai levantar um erro (Raise).
            self.set_login_senha(login_senha)
            email = input("Digite seu email: ")
            self.set_email(email)
            break
       
