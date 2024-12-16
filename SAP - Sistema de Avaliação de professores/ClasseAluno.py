#Colinha sobre Tipos de ERROS by Alura rsrsrs
#NameError geralmente acontece quando tentamos usar uma variável que ainda não foi definida.
#KeyError acontece ao buscarmos por uma chave inexistente dentro de uma estrutura como um dicionário. !!!!!!!!!!!!!!!!!!!!!!!!

try:
    from ClasseUsuario import *
    from datetime import datetime
    from ClasseErros import *

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
                try:
                    nome = str(input("Digite seu nome: "))
                    self.set_nome(nome)
                    
                    idade = int(input("Digite sua idade:"))
                    self.set_idade(idade)

                    login_usuario = input("Cadastre um usuário: ")
                    self.set_login_usuario(login_usuario)

                    login_senha = input("Cadastre uma senha: ")
                    self.set_login_senha(login_senha)

                    self.__ano_escolar = input("Qual sua série?\n[1] - Primeiro ano\n[2] - Segundo ano\n[3] - Terceiro ano\n> ")
                    if self.__ano_escolar < "1" or self.__ano_escolar > "3":
                        print ("Coloque uma opção válida")
                        continue

                    print ("Digite seu curso o nome do seu curso:\nInformática\nQuímica\nEdificações\nEletrotécnica")
                    self.__curso = input("Coloque sua resposta: ").upper()
                    if self.__curso not in ["INFORMÁTICA", "QUÍMICA", "ELETROTÉCNICA", "EDIFICAÇÕES"]:
                        print("Curso inválido! Escolha entre: INFORMÁTICA, QUÍMICA, ELETROTÉCNICA ou EDIFICAÇÕES.")
                    else:
                        print ("Cadastro Finalizado")
                        break
                    
                except NumError:
                    print("O nome não pode conter números, caracteres como virgula ou pontos e espaços em branco.") 
                    
                except ValueError:
                    print("Insira um número, sendo este do tipo inteiro.")
                    print("Reiniciando o processo...")
                

        def escreverAvaliacao(self):
            try:
                avalicacao_escrita = input("Escreva sua avaliação\n> ")
            except NameError:
                print("Insira uma resposta válida!")
            dataehora = datetime.now()
            return avalicacao_escrita, dataehora
except IndentationError:
    print("ERRO DE IDENTAÇÃO, VERIFIQUE SE HÁ PARÊNTESES FALTANDO, VÍRGULA OU PONTOS TROCADOS")
