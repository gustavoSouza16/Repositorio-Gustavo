from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseAluno import Aluno
from ClasseAvaliacao import Avaliacao
from datetime import datetime
from ClasseMural import*
from ClasseChefia import *
from ClasseProfessor import*

class Professor(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, salario, disciplina_ministrada):
        super().__init__(nome, idade, login_usuario,login_senha)
        self.__salario = salario
        self.__disciplina_ministrada = disciplina_ministrada

    def get_avaliacao(self):
        return self.__avaliacao

    def get_salario(self):
        return(self.__salario)

    def set_salario(self,novo_salario):
        self.__salario = novo_salario

    def get_disciplina_ministrada(self):
        return(self.__disciplina_ministrada)

    def set_disciplina_ministrada(self,nova_disciplina,):
        self.__disciplina_ministrada = nova_disciplina

    def cadastrar(self):
        try:
            nome = input("Insira seu nome: ")
            self.set_nome(nome)
            
            idade = int(input("Insira sua idade:"))
            if idade <= 0:
                raise ValueError('A idade precisa ser um número positivo, portanto, maior que 0.')          #Tratamento de exceção caso o valor seja negativo utilizando o Raise
            self.set_idade(idade)


            login_usuario = input("Cadastre um usuário: ")
            self.set_login_usuario(login_usuario)

            login_senha = input("Cadastre uma senha: ")
            self.set_login_senha(login_senha)

            salario = int(input("Insira seu salário: "))
            if salario <= 0:
                raise ValueError('Seu salário precisa ser um número positivo, portanto, maior que 0.')      #Tratamento de exceção caso o valor seja negativo utilizando o Raise
            self.set_salario(salario)

            disciplina_ministrada = input("Digite a disciplina que você ministra: ")
            self.set_disciplina_ministrada(disciplina_ministrada)

        except ValueError:                      
            print('Esse valor não é aceito, insira um valor válido.')       #Inserção do comando de exceção caso o valor esteja errado.

        except AttributeError:
            print('Esse atributo não é aceito, insira um valor válido.')    #Inserção do comando de exceção caso o atributo esteja errado.

        except Exception:
            print('Ocorreu um erro inesperado, tente novamente.')           #Inserção do comando de exceção caso algum erro não esperado ocorra.

        else:
            print('Cadastro realizado com sucesso.')

    def visualizarMural(self,mural):
        try:
            mural.consultarAvaliacao()          #Associação
        except AttributeError:   
            print('Esse atributo não é aceito, insira um valor válido.')     #Inserção do comando de exceção caso o valor esteja errado.
        except Exception:
            print('Ocorreu um erro ao tentar visualizar o mural.')           #Inserção do comando de exceção caso algum erro não esperado ocorra.
        finally:
            print('Finalizando a consulta no mural.')   
                                                                 
        

