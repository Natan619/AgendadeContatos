from contato import Contato

class AgendaContatos:
    """Classe para geranciar uma agenda de contatos."""
    def __init__ (self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        """Adiciona um novo contato à agenda."""
        contato = Contato(nome, telefone, email)
        if contato.validar_email() and contato.validar_telefone():
          self.contatos.append(contato) 
          print("Contato adicionado com sucesso!") 
        else:
            if not contato.validar_email():
             print("Erro: E-mail inválido")  
            if not contato.validar_telefone():
             print("Erro: Telefone inválido")  

    def visualizar_contatos(self):
        """Exibe todos os contatos da agenda"""
        if not self.contatos:
            print("Nenhum contato encontrado.")
        for contato in self.contatos:
            print(contato)   

    def excluir_contato(self, nome):
        """Excluí contato com base no nome selecionado"""
        for contato in self.contatos:
            if contato.name == nome:
                self.contatos.remove(contato)
                return
        print("Contato não encontrado")
