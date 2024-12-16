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
        try:                # Utilização dos comandos de exceção 
            nome = input("Insira seu nome: ")
            self.set_nome(nome)

            idade = int(input("Insira sua idade:"))
            if idade <= 0:
                raise ValueError('A idade precisa ser um número positivo, portanto, maior que 0.')
            self.set_idade(idade)


            login_usuario = input("Cadastre um usuário: ")
            self.set_login_usuario(login_usuario)       

            login_senha = input("Cadastre uma senha: ")
            self.set_login_senha(login_senha)

            while True:
                self.__ano_escolar = input("Qual sua série?\n[1] - Primeiro ano\n[2] - Segundo ano\n[3] - Terceiro ano\n> ")
                if self.__ano_escolar == "1" or self.__ano_escolar == "2" or self.__ano_escolar == "3":
                    break  
                else:
                    print("Coloque uma resposta válida.")
            
            while True:
                print("Digite o nome do seu curso:\nInformática\nQuímica\nEdificações\nEletrotécnica")
                self.__curso = input("Coloque sua resposta: ").upper()
                if self.__curso in ['INFORMÁTICA', 'QUÍMICA', 'EDIFICAÇÕES', 'ELETROTÉCNICA']:
                    break  
                else:
                    print("Coloque uma opção válida.")
                

        except ValueError as e:         # Utilização dos comandos de exceção 
            print(f'Erro:{e}')
        finally:                        # Utilização dos comandos de exceção 
            print('Cadastro concluído!')
                
    def escreverAvaliacao(self):
        avalicacao_escrita = input("Escreva sua avaliação\n> ")
        dataehora = datetime.now()
        return avalicacao_escrita, dataehora
