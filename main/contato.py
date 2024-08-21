class Contato:
    """Classe para representar um contato"""
    def __init__(self, nome, telefone, email):
        self.name = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.name}, Telefone: {self.telefone},  E-mail: {self.email}"
    