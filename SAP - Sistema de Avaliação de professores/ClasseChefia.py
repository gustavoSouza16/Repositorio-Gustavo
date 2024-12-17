from ClasseUsuario import*
from random import *

class ChefiaImediata(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, email, idChefia):
        super().__init__(nome, idade, login_usuario,login_senha)
        self.__email = email
        self.__idChefia = idChefia

    def get_idChefia(self):
        return self.__idChefia

    def get_email(self):
        return self.__email

    def set_idChefia(self, novoID):
        self.__idChefia = novoID

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
            try:
                nome = input("Digite seu nome: ")
                self.set_nome(nome)

                idade = int(input("Digite sua idade:"))
                self.set_idade(idade)

                login_usuario = input("Cadastre um usuário: ")
                self.set_login_usuario(login_usuario)

                login_senha = input("Cadastre uma senha: ")
                self.set_login_senha(login_senha)

                email = input("Digite seu email: ")
                self.set_email(email)
                break

            except StrError:
                print("Insira um número, sendo este do tipo inteiro.")
                print("Reiniciando o processo...")
            
            except NumError:
                print("O nome não pode conter números.")
            
            except ValueError:
                print("Sua idade não pode conter Letras, caracteres como virgula ou pontos e espaços em branco.")
       
