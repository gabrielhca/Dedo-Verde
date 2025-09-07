from planta import Planta

# gerencia uma coleção de objetos Plantas, permitindo adicionar
# listar, registrar observações e mostrar detalhes.
class GerenciadorPlantas:
    
    # inicia o gerenciador de plantas e adiciona os dados iniciais
    def __init__(self, dados_iniciais=None):
        self.plantas = {}
        if dados_iniciais:
            for nome, dados in dados_iniciais.items():
                nova_planta = Planta(nome, dados['descricao'])
                for obs in dados['observacoes']:
                    nova_planta.registrar_observacao(obs)
                self.plantas[nome] = nova_planta

    # permite adicionar uma nova especie ao banco de dados
    def adicionar_especie(self, nome, descricao):
        if nome in self.plantas:
            print(f"Erro: A espécie '{nome}' já foi registrada.")
            return

        # cria uma nova instancia e adiciona ao dicionario
        nova_planta = Planta(nome, descricao)
        self.plantas[nome] = nova_planta
        print(f"Espécie {nome} registrada com sucesso!")

    # registra uma nova observação para uma espécie existente
    def registrar_observacao(self, nome, observacao):
        planta = self.plantas.get(nome)
        if planta:
            # Chama o método da instancia de Planta
            planta.registrar_observacao(observacao) 
            print(f"Observação registrada para {nome}.")
        else:
            print(f"Erro: Espécie {nome} não encontrada.")

    # mostra a lista de todas as espécies registradas no banco de dados
    def listar_especies(self):
        print("\nLista de Espécies")
        if not self.plantas:
            print("Nenhuma espécie foi registrada ainda.")
        else:
            for especie in self.plantas.keys():
                print(f"{especie}")

    # exibe todos os detalhes de uma espécie, incluindo seu historico
    def mostrar_detalhes(self, nome):
        planta = self.plantas.get(nome)
        if planta:
            print(planta) 
        else:
            print(f"Erro: Espécie {nome} não encontrada.")
        