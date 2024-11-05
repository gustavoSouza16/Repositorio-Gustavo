#2°Ano Vespertino - Informática, Programação Orientada a Objetos
#Integrantes: Gabriel Lima Rosa, Gustavo Neves, Luiz Guilherme, Wellington Pereira
from classes import*
from database import*
from objetosPoo import*
from classealunoo import Aluno
from classeavaliacaoo import Avaliacao
from datetime import datetime
from classemural import*
from classechefia import *
from classeprofessor import*


def VasculharNomeProfessor():
    for professores in dicionario_de_profs_cadastrados:
        professor = dicionario_de_profs_cadastrados[professores]
        print (professor[0])


Carlos = Aluno("Carlos", 16, "Carlos123", "Carlos21", "1", "INFORMÁTICA")
conteudo = Carlos.escreverAvaliacao()
avaliacao = Avaliacao("133333", conteudo , "horaAvaliacao", "remetenteAvaliacao", "destinatarioAvaliacao")
print (avaliacao.get_conteudoAvaliacao())
mural = Mural()
while True:
    print("-" * 12, "MENU DO SAP", "-" * 12)
    print("\n1 - Cadastrar Usuário\n2 - Logar com uma conta\n3 - Sair")
    opcao = input(">")


    if opcao == "1":
        print("\nCadastrar como:\n[1] - Aluno\n[2] - Professor")
        cadastrar_usuario = input("Coloque sua resposta:\n> ")




        if cadastrar_usuario == "1":
            criar_usuario_obj = Aluno(0,0,0,0,0,0)
            criar_usuario_obj.cadastrar()
            dicionario_de_usuario_alunos_cadastrados[criar_usuario_obj.get_login_usuario()] = f"{criar_usuario_obj.get_nome()}", (criar_usuario_obj.get_idade()), f"{criar_usuario_obj.get_login_usuario()}", f"{criar_usuario_obj.get_login_senha()}", f"{criar_usuario_obj.get_ano_escolar()}", f"{criar_usuario_obj.get_curso()}"
            print(f"Você foi cadastrado {criar_usuario_obj.get_nome()}")




        elif cadastrar_usuario == "2":
            criar_usuario_obj = Professor(0,0,0,0,0,0)
            criar_usuario_obj.cadastrar()
            dicionario_de_profs_cadastrados[criar_usuario_obj.get_login_usuario()] = f"{criar_usuario_obj.get_nome()}", criar_usuario_obj.get_idade(), f"{criar_usuario_obj.get_login_usuario()}", f"{criar_usuario_obj.get_login_senha()}", criar_usuario_obj.get_salario() , f"{criar_usuario_obj.get_disciplina_ministrada()}"
            print(f"Você foi cadastrado {criar_usuario_obj.get_nome()}")

        elif cadastrar_usuario == "3":
            criar_usuario_obj = ChefiaImediata(0,0,0,0,0,0)
            criar_usuario_obj.cadastrar()
            dicionario_de_chefia[criar_usuario_obj.get_login_usuario()] = f"{criar_usuario_obj.get_nome()}", criar_usuario_obj.get_idade(), f"{criar_usuario_obj.get_login_usuario()}", f"{criar_usuario_obj.get_login_senha()}", criar_usuario_obj.get_idChefia() , f"{criar_usuario_obj.get_email()}"
            print(f"Você foi cadastrado {criar_usuario_obj.get_nome()}")
        
        else:
            print("Coloque uma resposta válida")
        
    elif opcao == "2":
        print("\nRealizar login como:\n[1] - Aluno\n[2] - Professor")
        tipo_usuario = input("Coloque sua resposta:\n> ")
        if tipo_usuario == "1":
            login_usuario = input("Coloque seu usuário para login:")
            login_senha = input("Coloque sua senha para login:")
        logar(login_usuario, login_senha,dicionario_de_usuario_alunos_cadastrados)
        opcao_escrever = input("[1] Escrever Avaliação de professor\n[2] Retornar ao menu")


        if opcao_escrever == "1":

            usuario = dicionario_de_usuario_alunos_cadastrados[login_usuario]
            Aluno_logado = Aluno (usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
            usuario_profs = [professor for professor in dicionario_de_profs_cadastrados.keys()]
            print (usuario_profs)
            DadoProfessor = input("Por favor, coloque o usuário do professor a quem deseja avaliar")  #OBS: INVERTER POSIÇÕES, PARA PERGUNTAR A QUE PROF DESEJA ENVIAR PRIMEIRO E DEPOIS AVALIAR
            Professor1 = dicionario_de_profs_cadastrados[DadoProfessor]
            ProfessorCitado = Professor(Professor1[0],Professor1[1],Professor1[2],Professor1[3],Professor1[4],Professor1[5])
            if DadoProfessor not in usuario_profs:
                print ("Coloque uma resposta válida")
                continue
            else:
                conteudo = Aluno_logado.escreverAvaliacao()                                                            
                avaliacao = Avaliacao(0, conteudo , conteudo, Aluno_logado, ProfessorCitado)                                         #Associação    
                mural.adicionarAvaliacao(avaliacao)                                                                      #Agregação
                mural.consultarAvaliacao()
                print("Sua avaliação está completa")

        elif tipo_usuario == "2":
            login_usuario = input("Coloque seu usuário para login:")
            login_senha = input("Coloque sua senha para login:")
            logar(login_usuario, login_senha, dicionario_de_profs_cadastrados)
            
        elif tipo_usuario == "3":
            login_usuario = input("Coloque seu usuário para login:")
            login_senha = input("Coloque sua senha para login:")
            logar(login_usuario, login_senha, dicionario_de_chefia) 


        


    elif opcao == "3":
        print("Bem, Adeus")
        break
