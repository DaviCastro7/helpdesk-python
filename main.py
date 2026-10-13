chamados = []
def exibir_menu():
    print("\n========== HELPDESK PYTHON ==========")
    print("1 - Abrir novo chamado")
    print("2 - Listar chamados")
    print("3 - Consultar chamado")
    print("4 - Sair")
    print("====================================")

def cadastrar_chamado():
    print("\n--- ABERTURA DE CHAMADO ---")

    titulo = input("Insira o título do problema: ")
    descricao = input("Descreva o seu problema: ")

    novo_id = len(chamados) + 1

    chamado = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": "Aberto"
    }
    chamados.append(chamado)

    print("\nChamado registrado:")
    print(chamado)

def listar_chamados():
    print("\n--- LISTA DE CHAMADOS ---")

    if not chamados:
        print("Nenhum chamado cadastrado.")
        return

    for chamado in chamados:
        print("----------------------------")
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Descrição: {chamado['descricao']}")
        print(f"Status: {chamado['status']}")


def consultar_chamado():
    print("\n--- CONSULTAR CHAMADO ---")

    id_busca = input("Insira o ID do chamado: ")

    for chamado in chamados:
        if str(chamado["id"]) == id_busca:
            print("\nChamado encontrado!")
            print(f"ID: {chamado['id']}")
            print(f"Título: {chamado['titulo']}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Status: {chamado['status']}")
            return

    print("Chamado não encontrado.")



def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_chamado()

        elif opcao == "2":
            listar_chamados()

        elif opcao == "3":
            consultar_chamado()
        elif opcao == "4":
            print("Encerrando o HelpDesk Python...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
