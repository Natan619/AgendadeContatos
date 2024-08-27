import re

class Contato:
    """Classe para representar um contato"""
    def __init__(self, nome, telefone, email):
        self.name = nome.strip()
        self.telefone = telefone.strip()
        self.email = email.strip()
    
    def validar_email(self):
        padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(padrao_email, self.email) is not None
    
    def validar_telefone(self):
        padrao_telefone = r'^\d{11}$'
        return re.match(padrao_telefone, self.telefone) is not None

    def __str__(self):
        return f"Nome: {self.name}, Telefone: {self.telefone},  E-mail: {self.email}"
    
    
