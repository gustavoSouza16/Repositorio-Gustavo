from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseAluno import *
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
        if not str(novo_salario).isdigit():
            raise SalarioError()
        self.__salario = int(novo_salario)

    def get_disciplina_ministrada(self):
        return(self.__disciplina_ministrada)

    def set_disciplina_ministrada(self,nova_disciplina):
         if not nova_disciplina.isalpha():
            raise DisciplinaErro
         self.__disciplina_ministrada = nova_disciplina
         
    def cadastrar(self):
        while True:
            try:
                nome = input("Digite seu nome: ")
                self.set_nome(nome)

                idade = input("Digite sua idade:") 
                self.set_idade(idade)

                login_usuario = input("Cadastre um usuário: ")
                self.set_login_usuario(login_usuario)

                login_senha = input("Cadastre uma senha: ")
                self.set_login_senha(login_senha)

                salario = input("Digite seu salário: ")
                self.set_salario(salario)

                disciplina_ministrada = input("Digite a disciplina que você ministra: ")
                self.set_disciplina_ministrada(disciplina_ministrada)
                break
            
            except ValueError:
                print("Sua idade não pode conter Letras, caracteres como virgula ou pontos e espaços em branco.")

            except DisciplinaErro:
                print("A Disciplina não pode conter números, apenas algarismos romanos se precisar.")

            except SalarioError:
                print("Utilize apenas números!")   

            except NumError:
                 print("O nome não pode conter números, caracteres como virgula ou pontos e espaços em branco.")
             

    def visualizarMural(self, mural):
        mural.consultarAvaliacao()                                                              #Associação
        

