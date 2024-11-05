class Mural:
    def __init__(self, idMural, quantidadeAvaliacao, descricao, avaliacoesAprovados):
        self.idMural = idMural
        self.quantidadeAvaliacao = quantidadeAvaliacao
        self.descricao = descricao
        self.avaliacoesAprovados = avaliacoesAprovados

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
