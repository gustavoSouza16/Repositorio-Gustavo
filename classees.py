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

class Aluno(UsuarioIfro):

    def __init__(self, nome, idade, login_usuario,login_senha,ano_escolar, curso):
        super().__init__(nome, idade, login_usuario,login_senha)
        self._ano_escolar = ano_escolar
        self._curso = curso


    def get_ano_escolar(self):
        return self._ano_escolar

    def set_ano_escolar(self, novo_ano_escolar):
        self._ano_escolar = novo_ano_escolar        

    def get_curso(self):
        return self._curso

    def set_curso(self, novo_curso):
        self._curso = novo_curso

    def cadastrar(self):
        while True:
            self.nome = input("Digite seu nome: ")
            self.idade = int(input("Digite sua idade:"))
            self._login_usuario = input("Cadastre um usuário: ")
            self._login_senha = input("Cadastre uma senha: ")
            self._ano_escolar = input("Qual sua série?\n[1] - Primeiro ano\n[2] - Segundo ano\n[3] - Terceiro ano\n> ")
            if self._ano_escolar != "1" and self._ano_escolar != "2" and self._ano_escolar != "3":
                print ("Coloque uma resposta válida.")
                continue
            print ("Digite seu curso o nome do seu curso:\nInformática\nQuímica\nEdificações\nEletrotécnica")
            self._curso = input("Coloque sua resposta: ").upper()
            if self._curso != 'INFORMÁTICA' and self._curso != 'QUÍMICA' and self._curso != 'EDIFICAÇÕES' and  self._curso != 'ELETROTÉCNICA':
                print ("Coloque uma opção válida")
                continue
            else:
                print ("Cadastro Finalizado")
                break



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

