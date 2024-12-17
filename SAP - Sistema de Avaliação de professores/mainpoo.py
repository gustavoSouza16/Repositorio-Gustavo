#2°Ano Vespertino - Informática, Programação Orientada a Objetos
#Integrantes: Gabriel Lima Rosa, Gustavo Neves, Luiz Guilherme, Wellington Pereira
#BRANCH - LUIZ GUILHERME
from ClasseUsuario import*
from dicionario import*
from instancias import*
from ClasseAluno import Aluno
from ClasseAvaliacao import Avaliacao
from datetime import datetime
from ClasseMural import*
from ClasseChefia import *
from ClasseProfessor import*

def VasculharNomeProfessor():
    for professores in dicionario_de_profs_cadastrados:
        professor = dicionario_de_profs_cadastrados[professores]
        print (professor[0])

mural = Mural()
while True:
    print("-" * 12, "MENU DO SAP", "-" * 12)
    print("\n1 - Cadastrar Usuário\n2 - Logar com uma conta\n3 - Sair")
    opcao = input(">")
    
    if opcao == "1":
        print("\nCadastrar como:\n[1] - Aluno\n[2] - Professor\n[3] - Chefia Imediata")
        cadastrar_usuario = input("Coloque sua resposta:\n> ")
        if cadastrar_usuario == "1":                                                                            #MODIFICAR PARA NÚMEROS REAIS AO INVÉS DE STRINGS
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
        print("\nRealizar login como:\n[1] - Aluno\n[2] - Professor\n[3] - Chefia Imediata")
        tipo_usuario = input("Coloque sua resposta:\n> ")
        if tipo_usuario == "1":
            login_usuario = input("Coloque seu usuário para login:")
            login_senha = input("Coloque sua senha para login:")
            op = logar(login_usuario, login_senha,dicionario_de_usuario_alunos_cadastrados)
            if op == True:
                opcao_escrever = input("[1] - Escrever Avaliação de professor\n[2] - Retornar ao menu")
                if opcao_escrever == "1":
                    usuario = dicionario_de_usuario_alunos_cadastrados[login_usuario]
                    Aluno_logado = Aluno (usuario[0],usuario[1],usuario[2],usuario[3],usuario[4],usuario[5])
                    usuario_profs = [professor for professor in dicionario_de_profs_cadastrados.keys()]
                    print (usuario_profs)
                    DadoProfessor = input("Por favor, coloque o usuário do professor a quem deseja avaliar\n>") 
                    Professor1 = dicionario_de_profs_cadastrados[DadoProfessor]
                    ProfessorCitado = Professor(Professor1[0],Professor1[1],Professor1[2],Professor1[3],Professor1[4],Professor1[5])
                elif opcao_escrever == "2":
                    continue
                else:                                     
                    continue
                if DadoProfessor not in usuario_profs:                                            #TALVEZ DÊ PARA REMOVER UTILIZANDO O TRY EXCEPT NO DICIONÁRIO, ITEM A SER OBSERVADO
                    print ("Coloque uma resposta válida")
                    continue
                else:
                    conteudo = Aluno_logado.escreverAvaliacao()                                                                                              
                    avaliacao = Avaliacao(conteudo , conteudo, Aluno_logado, ProfessorCitado)                                         #Associação    
                    AvaliacoesAndamento.append(avaliacao)
                    mural.adicionarAvaliacao(avaliacao)                                                                               #Agregação
                    print("Sua avaliação está completa")
            if op == False:
                continue

        elif tipo_usuario == "2":
            login_usuario = input("Coloque seu usuário para login:")
            login_senha = input("Coloque sua senha para login:")
            op = logar(login_usuario, login_senha, dicionario_de_profs_cadastrados)
            if op == True:
                visu = input("[1] - Visualizar o Mural de Avaliações\n[2] - Retornar ao menu")
                if visu == "1":
                    prof = dicionario_de_profs_cadastrados[login_usuario]
                    prof_logado = Professor(prof[0], prof[1], prof[2], prof[3], prof[4], prof[5])
                    prof_logado.visualizarMural(mural)                                                                                #Associação
                if visu == "2":
                    continue
                else:
                    continue
            if op == False:
                continue

        elif tipo_usuario == "3":
            login_usuario = input("Coloque seu usuário para login:")
            login_senha = input("Coloque sua senha para login:")
            op = logar(login_usuario, login_senha, dicionario_de_chefia)
            if op == True:
                viwer = input("[1] - Revisar avaliações\n[2] - Retornar ao menu")   
                if viwer == "1":
                    chefia = dicionario_de_chefia[login_usuario]
                    chefiaIm = ChefiaImediata(chefia[0],chefia[1],chefia[2],chefia[3],chefia[4],chefia[5])
                    for i, ItemsAvaliacao in enumerate(AvaliacoesAndamento, start=1):
                        ItemsAvaliacao.set_idAvaliacao(i)
                        print ("-"*100,f"\n\n{ItemsAvaliacao.gerarAvaliacao()}","-"*100)
                    revisar = input(("Coloque o Id da avaliação que você deseja Aprovar ou Reprovar"))
                    coletarAvaliacaoId = None
                    for avaliacaooo in AvaliacoesAndamento:
                        if avaliacaooo.get_idAvaliacao() == revisar:
                            coletarAvaliacaoId = avaliacaooo
                            aprovareprovar = input("Você deseja aprovar ou reprovar essa avaliação? \n[1] - Aprovar\n[2] - Reprovar\n>")
                            if aprovareprovar == "1":
                                chefia.aprovarAvaliacao(mural,coletarAvaliacaoId)                                                               #Associação
                            elif aprovareprovar == "2":
                                chefia.reprovarAvaliacao()
                            break
                        else:
                            print("ID incorreto")
                            break

                elif viwer == "2":
                    continue

            elif op == False:
                continue

    elif opcao == "3":
        print("Bem, Adeus")
        break

