class Mural:
    def __init__(self):
        self.idMural = None
        self.quantidadeAvaliacao = None
        self.descricao = None
        self.avaliacoesAprovados = []


#metodos
    def adicionarAvaliacao(self, Avaliacao):
        self.avaliacoesAprovados.append(Avaliacao)


    def removerAvaliacao(self, idAvaliacao):
        pass
    def consultarAvaliacao(self):
        print("*"*40)
        for avaliacao in self.avaliacoesAprovados:
            print (avaliacao.get_conteudoAvaliacao(),avaliacao.get_remetenteAvaliacao(), avaliacao.get_destinatarioAvaliacao(), avaliacao.get_respostaAvaliacao())
        print("*"*40)
    def consultarDescricao(self):
        print("O mural é o local onde o usuário pode inserir suas avaliações feitas para um docente de sua instituição e ver outras avaliações realizadas por outros discentes.")

