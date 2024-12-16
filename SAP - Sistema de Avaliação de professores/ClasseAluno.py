#Colinha sobre Tipos de ERROS by Alura rsrsrs
#NameError geralmente acontece quando tentamos usar uma variável que ainda não foi definida.
#KeyError acontece ao buscarmos por uma chave inexistente dentro de uma estrutura como um dicionário. !!!!!!!!!!!!!!!!!!!!!!!!

try:
    from ClasseUsuario import *
    from datetime import datetime

    class Aluno(UsuarioIfro):

        def __init__(self, nome, idade, login_usuario,login_senha,ano_escolar, curso):
            super().__init__(nome, idade, login_usuario,login_senha)
            self.__ano_escolar = ano_escolar
            self.__curso = curso

        def get_ano_escolar(self):
            return self.__ano_escolar

        def set_ano_escolar(self, novo_ano_escolar):
            self.__ano_escolar = novo_ano_escolar        
            
        def get_curso(self):
            return self.__curso
            
        def set_curso(self, novo_curso):
            self.__curso = novo_curso
            
        def cadastrar(self):
            while True:
 
                    nome = str(input("Digite seu nome: "))
                    self.set_nome(nome)
                    try:
                        idade = int(input("Digite sua idade:"))
                        self.set_idade(idade)
                    except ValueError:
                        print("Insira um número, sendo este do tipo inteiro.")
                        print("Reiniciando o processo...")
                        continue
                    login_usuario = input("Cadastre um usuário: ")
                    self.set_login_usuario(login_usuario)
                    login_senha = input("Cadastre uma senha: ")
                    self.set_login_senha(login_senha)
                    self.__ano_escolar = input("Qual sua série?\n[1] - Primeiro ano\n[2] - Segundo ano\n[3] - Terceiro ano\n> ")
                    if self.__ano_escolar < "1" or self.__ano_escolar > "3":
                         print("Digite um número inteiro sendo ele entre 1, 2 ou 3.")
                         continue
                    print ("Digite seu curso o nome do seu curso:\nInformática\nQuímica\nEdificações\nEletrotécnica")
                    self.__curso = input("Coloque sua resposta: ").upper()
                    if self.__curso not in ["INFORMÁTICA", "QUÍMICA", "ELETROTÉCNICA", "EDIFICAÇÕES"]:
                        print ("Coloque uma opção válida")
                        continue
                    else:
                        print ("Cadastro Finalizado")
                        break

                    
        def escreverAvaliacao(self):
            avalicacao_escrita = input("Escreva sua avaliação\n> ")
            dataehora = datetime.now()
            return avalicacao_escrita, dataehora
except IndentationError:
    print("ERRO DE IDENTAÇÃO, VERIFIQUE SE HÁ PARÊNTESES FALTANDO, VÍRGULA OU PONTOS TROCADOS")
