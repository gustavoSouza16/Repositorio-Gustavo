from classes import *

class Professor(UsuarioIfro):
    def __init__(self, nome, idade, login_usuario,login_senha, salario, disciplina_ministrada):
        super().__init__(nome, idade, login_usuario,login_senha)
        self._salario = salario
        self.disciplina_ministrada = disciplina_ministrada

    def get_salario(self):
        return(self._salario)

    def set_salario(self,novo_salario):
        self._salario = novo_salario

    def get_disciplina_ministrada(self):
        return(self.disciplina_ministrada)

    def set_disciplina_ministrada(self,nova_disciplina,):
        self.disciplina_ministrada = nova_disciplina

    def cadastrar(self):
        self.nome = input("Digite seu nome: ")
        self.idade = int(input("Digite sua idade:"))
        self._login_usuario = input("Cadastre um usuário: ")
        self._login_senha = input("Cadastre uma senha: ")
        self._salario = int(input("Digite seu salário: "))
        self.disciplina_ministrada = input("Digite a disciplina que você ministra: ")

    def responderAvaliacao(self, avaliacao):
        pass
