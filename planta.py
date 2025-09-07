# Representa uma planta com sua sinformações e historico de observações

class Planta:

    # __init__ é o construtor
    # 'self' é uma referencia a instancia da classe
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.observacoes = []

    def registrar_observacao(self, observacao):
        # adiciona uma nova observacao ao historico da planta
        self.observacoes.append(observacao)

    def __str__(self):
        # retorna uma representação em string da planta, exibindo seus detalhes
        detalhes = f"\nDetalhes de {self.nome}"
        detalhes += f"Descricao: {self.descricao}"
        detalhes += "Observações:\n"
        if not self.observacoes:
            detalhes += " Nenhuma observacao foi registrada ainda.\n"
        else:
            for obs in self.observacoes:
                detalhes += f" - {obs}\n"
        return detalhes