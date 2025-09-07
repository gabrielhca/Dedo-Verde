from gerenciador import GerenciadorPlantas

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
main
"""

def main():

    gerenciador = GerenciadorPlantas(dados_iniciais=banco_de_dados)

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
            gerenciador.adicionar_especie(nome, descr)
        elif escolha == '2':
            nome = input("Qual espécie você observou? ")
            obs = input("Descreva sua observação: ")
            gerenciador.registrar_observacao(nome, obs)
        elif escolha == '3':
            gerenciador.listar_especies()
        elif escolha == '4':
            nome = input("Qual nome da espécie que você quer ver detalhes? ")
            gerenciador.mostrar_detalhes(nome)
        elif escolha == '5':
            print("Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# boa pratica: garante que o codigo so seja executao quando o arquivo é o programa principal
if __name__ == "__main__":
    main()