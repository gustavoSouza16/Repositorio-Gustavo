dicionario_de_usuario_alunos_cadastrados = {}
dicionario_de_profs_cadastrados = {}
dicionario_de_chefia = {}
AvaliacoesAndamento = []

def logar(login_usuario, login_senha, dicionario):
    if login_usuario in dicionario:
        usuario = dicionario[login_usuario]
        if login_senha == usuario[3]:
            print(f"Você está logado, BEM VINDO {usuario[0]}!")
            return True
        else:
            print("USUÁRIO OU SENHA INCORRETO!")
            return False
    else:
        print("USUÁRIO OU SENHA INCORRETO!")
        return False
    

