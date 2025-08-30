"""
'banco_de_dados' é o dicionário externo que guarda outras estruturas de dicionários,
cada um dos dicionarios internos são representados uma planta diferente, 
a chave de observações contem uma lista de registros.
"""

banco_de_dados = {
    "Zamioculca": {
        "descricao": "Planta de interior, fácil de cuidar e resistente à falta de luz.",
        "observacoes": [
            "28/08/2025: Regada e colocada em um novo vaso.",
            "20/08/2025: Uma nova folha começou a crescer."
        ]
    },
    "Espada de São Jorge": {
        "descricao": "Planta com folhas longas e rígidas, conhecida por purificar o ar.",
        "observacoes": [
            "23/08/2025: Aparenta estar saudável. Nenhuma mudança visível."
        ]
    },
    "Jiboia": {
        "descricao": "Planta trepadeira com folhas em forma de coração, ideal para pendurar.",
        "observacoes": []
    }
}

"""
funções
"""

def adicionar_especie(nome, descricao):
    # permite adicionar uma nova espécie ao banco de dados
    if nome in banco_de_dados:
        print(f"Erro: A espécie '{nome}' já foi registrada.")
        return
    # cria um dicionario interno para nova espécie.
    nova_especie = {
        "descricao": descricao,
        "observacoes": []
    }
    # adiciona o novo dicionario ao banco de dados
    banco_de_dados[nome] = nova_especie
    print(f"Espécie {nome} registrada com sucesso!")

def registrar_observacao(nome, observacao):
    # registra uma nova observação para uma espécie existente
    if nome in banco_de_dados:
        banco_de_dados[nome]["observacoes"].append(observacao) # apeend() adiciona um valor ao final da lista
        print(f"Observação registrada para {nome}.")
    else:
        print(f"Erro: Espécie {nome} não encontrada.")

def listar_especies():
    # mostra a lista de todas as espécies registradas no banco de dados
    print("Lista de Espécies")
    if not banco_de_dados:
        print("Nenhuma espécie foi registrada ainda.")
    else:
        for especie in banco_de_dados.keys():
            print(f"{especie}")

def mostrar_detalhes(nome):
    # exibe todos os detalhes de uma espécie, incluindo seu historico.
    if nome in banco_de_dados:
        dados_especie = banco_de_dados[nome]
        print(f"\n Detalhes de: {nome}")
        print(f"Descrição: {dados_especie['descricao']}")
        print("Observações:")
        for obs in dados_especie["observacoes"]:
            print(f"- {obs}")
    else:
        print(f"Erro: Espécie {nome} não encontrada.")

"""
main
"""

def main():
    # funçao principal
    while True:
        print("\n Menu Principal - Dedo Verde")
        print("1. Adicionar nova espécie")
        print("2. Registrar uma observação")
        print("3. Listar todas as espécies")
        print("4. Mostrar detalhes de uma espécie")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Qual nome da nova espécie? ")
            descr = input("Escreva a descrição da espécie: ")
            adicionar_especie(nome, descr)
        elif escolha == '2':
            nome = input("Qual espécie você observou? ")
            obs = input("Descreva sua observação: ")
            registrar_observacao(nome, obs)
        elif escolha == '3':
            listar_especies()
        elif escolha == '4':
            nome = input("Qual nome da espécie que você quer ver detalhes? ")
            mostrar_detalhes(nome)
        elif escolha == '5':
            print("Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# boa pratica: garante que o codigo so seja executao quando o arquivo é o programa principal
if __name__ == "__main__":
    main()