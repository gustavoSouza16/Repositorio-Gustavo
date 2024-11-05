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
        print("*"*10)
        for avaliacao in self.avaliacoesAprovados:
            print (avaliacao.get_conteudoAvaliacao())
        print("*"*10)

    def consultarDescricao(self):
        print("O mural é o local onde o usuário pode inserir suas avaliações feitas para um docente de sua instituição e ver outras avaliações realizadas por outros discentes.")
