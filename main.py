
def exibir_menu():
    print("\n========== HELPDESK PYTHON ==========")
    print("1 - Abrir novo chamado")
    print("2 - Listar chamados")
    print("3 - Consultar chamado")
    print("4 - Sair")
    print("====================================")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Você escolheu abrir um chamado.")

        elif opcao == "2":
            print("Você escolheu listar os chamados.")

        elif opcao == "3":
            print("Você escolheu consultar um chamado.")

        elif opcao == "4":
            print("Encerrando o HelpDesk Python...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
