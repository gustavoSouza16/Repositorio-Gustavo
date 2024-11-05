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
        pass

