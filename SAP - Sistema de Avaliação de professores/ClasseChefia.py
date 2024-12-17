from ClasseUsuario import*
from random import *

class ChefiaImediata(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, email):
        super().__init__(nome, idade, login_usuario,login_senha)
        self.__email = email
        self.__idChefia = None

    def get_idChefia(self):
        return self.__idChefia

    def set_idChefia(self, novoID):
        self.__idChefia = novoID

    def get_email(self):
        return self.__email

    def set_email(self, novoEmail):
        self.__email = novoEmail

    def visualizarAvaliacao(self,avaliacao):
        return avaliacao.gerarAvaliacao()                                                                 #Relacionamento de Associação

    def aprovarAvaliacao(self, mural,avaliacao):
        print("Avaliação aprovada e sendo inserida QQno Mural")
        mural.adicionarAvaliacao(avaliacao)                                                               #Relacionamento de Agregação
        print ("Avaliação inserida e disponível para os professores destinatários vizualizarem")
        
    def reprovarAvaliacao(self):
        print ("A Avaliação foi reprovada.")

    def cadastrar(self):
        try:
            nome = input("Digite seu nome: ")
            self.set_nome(nome)

            idade = int(input("Digite sua idade: "))
            self.set_idade(idade)

            login_usuario = input("Cadastre um usuário: ")
            self.set_login_usuario(login_usuario)

            login_senha = input("Cadastre uma senha: ")
            self.set_login_senha(login_senha)

            email = input("Digite seu email: ")
            self.set_email(email)  

            self.set_idChefia(randint(1000, 9999))  
            print(f"Chefia imediata cadastrada com ID: {self.get_idChefia()}")
            
        except ValueError:                      
            print('Esse valor não é aceito, insira um valor válido.')       #Inserção do comando de exceção caso o valor esteja errado.

        except AttributeError:
            print('Esse atributo não é aceito, insira um valor válido.')    #Inserção do comando de exceção caso o atributo esteja errado.

        except Exception:
            print('Ocorreu um erro inesperado, tente novamente.')           #Inserção do comando de exceção caso algum erro não esperado ocorra.

        else:
            print('Cadastro realizado com sucesso.')
       
