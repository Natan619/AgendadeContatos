import sqlite3

class Database:
    def __init__(self, db_name="agenda_contatos.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        """Cria a tabela de contatos, se não existir."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL,           
                telefone TEXT NOT NULL,
                email TEXT NOT NULL            
            )
        """)
        self.connection.commit()

    def adicionar_contato(self, nome, telefone, email):
        """Adiciona um contato ao banco de dados."""
        self.cursor.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
        self.connection.commit()

    def visualizar_contatos(self):
        """Retorna todos os contatos do banco de dados."""
        self.cursor.execute("SELECT * FROM contatos")
        return self.cursor.fetchall()

    def excluir_contato(self, nome):
        """Exclui um contato do banco de dados."""
        self.cursor.execute("DELETE FROM contatos WHERE nome=?", (nome,))
        self.connection.commit()

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.connection.close()
