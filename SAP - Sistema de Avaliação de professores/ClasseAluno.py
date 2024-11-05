from ClasseAluno import *
from datetime import datetime

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

#escrever método escrever depois

    def escreverAvaliacao(self):
        avalicacao_escrita = input("Escreva sua avaliação\n> ")
        dataehora = datetime.now()
        return avalicacao_escrita, dataehora
