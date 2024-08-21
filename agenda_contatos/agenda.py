from contato import Contato

class AgendaContatos:
    """Classe para geranciar uma agenda de contatos."""
    def __init__ (self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        """Adiciona um novo contato à agenda."""
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)    

    def visualizar_contatos(self):
        """Exibe todos os contatos da agenda"""
        if not self.contatos:
            print("Nenhum contato encontrado.")
        for contato in self.contatos:
            print(contato)        