from contato import Contato
from database import Database

class AgendaContatos:
    """Classe para geranciar uma agenda de contatos usando SQLite. """
    def __init__ (self):
        self.db = Database()

    def adicionar_contato(self, nome, telefone, email):
        """Adiciona um novo contato no banco de dados."""
        contato = Contato(nome, telefone, email)
        if contato.validar_email() and contato.validar_telefone():
          self.db.adicionar_contato(nome, telefone, email)
          print("Contato adicionado com sucesso!") 
        else:
            if not contato.validar_email():
             print("Erro: E-mail inválido")  
            if not contato.validar_telefone():
             print("Erro: Telefone inválido")  

    def visualizar_contatos(self):
        """Exibe todos os contatos da agenda do banco de dados."""
        contatos = self.db.visualizar_contatos()
        return contatos  

    def excluir_contato(self, nome):
        """Excluí contato com base no nome selecionado do banco de dados"""
        self.db.excluir_contato(nome)
        print("Contato não encontrado")
