from agenda import AgendaContatos

class Menu:
    """Classe para exibir o menu e gerenciar interações com usuário."""
    def __init__(self):
        self.agenda = AgendaContatos()

    def exibir_menu(self):
        """Exibe o menu e processa a opção escolhida pelo usuário."""
        while True:
            print("\nAgenda de Contatos")
            print("1. Adicionar Contato")
            print("2. Visualizar Contatos")
            print("3. Excluir Contato")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                email = input("E-mail: ")
                self.agenda.adicionar_contato(nome, telefone, email)

            elif opcao == "2":
                self.agenda.visualizar_contatos()

            elif opcao == "3":
                nome = input("Nome do contato para ser excluído: ")
                self.agenda.excluir_contato(nome)
                print("Contato excluído com seucesso!")

            elif opcao == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida! Tente novamnete.")
