from database import  dicionario_de_usuario_alunos_cadastrados, dicionario_de_profs_cadastrados
from classeprofessor import Professor
from classealunoo import Aluno




#Instâncias de Alunos


Thales = Aluno("Thales", 18, "Thales325", "Thales3024", "2", "QUÍMICA")
Seixas = Aluno("Seixas", 17, "Seixasbrabo", "Seixasincrível", "1","EDIFICAÇÕES")
Silvio = Aluno("Silvio", 19, "SilvioRei", "Silviolegal", "3", "ELETROTÉCNICA")


#Adicionando essas instâncias de aluno no dicionário de aluno






dicionario_de_usuario_alunos_cadastrados[Thales.get_login_usuario()] = f"{Thales.get_nome()}", Thales.get_idade(), f"{Thales.get_login_usuario()}", f"{Thales.get_login_senha()}", f"{Thales.get_ano_escolar()}", f"{Thales.get_curso()}"


dicionario_de_usuario_alunos_cadastrados[Seixas.get_login_usuario()] = f"{Seixas.get_nome()}", Seixas.get_idade(), f"{Seixas.get_login_usuario()}", f"{Seixas.get_login_senha()}", f"{Seixas.get_ano_escolar()}", f"{Seixas.get_curso()}"


dicionario_de_usuario_alunos_cadastrados[Silvio.get_login_usuario()] = f"{Silvio.get_nome()}", Silvio.get_idade(), f"{Silvio.get_login_usuario()}", f"{Silvio.get_login_senha()}", f"{Silvio.get_ano_escolar()}", f"{Silvio.get_curso()}"




#Instâncias de professores


Ozemar = Professor("Ozemar", 38, "Ozemar123", "Ozemar0402", 3000, "Matemática")
Julia = Professor("Julia", 22, "Julia423", "Julia3040", 3500, "Inglês")
Andre = Professor("André", 18, "André123", "André12", 5000,"Manutenção de Computadores")
Marcos = Professor("Marcos", 28, "Marcos1721", "Marcos2930", 5000,"Programação Orientada a Objetos")








#Adicionando essas instâncias de professor no dicionário de professor no dicionário








dicionario_de_profs_cadastrados[Ozemar.get_login_usuario()] = f"{Ozemar.get_nome()}", Ozemar.get_idade(), f"{Ozemar.get_login_usuario()}", f"{Ozemar.get_login_senha()}", Ozemar.get_salario(), f"{Ozemar.get_disciplina_ministrada()}"
dicionario_de_profs_cadastrados[Julia.get_login_usuario()] = f"{Julia.get_nome()}", Julia.get_idade(), f"{Julia.get_login_usuario()}", f"{Julia.get_login_senha()}", Julia.get_salario(), f"{Julia.get_disciplina_ministrada()}"
dicionario_de_profs_cadastrados[Andre.get_login_usuario()] = f"{Andre.get_nome()}", Andre.get_idade(), f"{Andre.get_login_usuario()}", f"{Andre.get_login_senha()}", Andre.get_salario(), f"{Andre.get_disciplina_ministrada()}"
dicionario_de_profs_cadastrados[Marcos.get_login_usuario()] = f"{Marcos.get_nome()}",Marcos.get_idade(), f"{Marcos.get_login_usuario()}", f"{Marcos.get_login_senha()}", Marcos.get_salario(), f"{Marcos.get_disciplina_ministrada()}"
