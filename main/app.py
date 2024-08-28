import tkinter as tk
from tkinter import messagebox
from agenda import AgendaContatos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contatos")

        self.agenda = AgendaContatos()

        # Campos de Entrada
        self.lbl_nome = tk.Label(root, text="Nome")
        self.lbl_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)

        self.lbl_telefone = tk.Label(root, text="Telefone")
        self.lbl_telefone.grid(row=1, column=0)
        self.entry_telefone = tk.Entry(root)
        self.entry_telefone.grid(row=1, column=1)

        self.lbl_email = tk.Label(root, text="E-mail")
        self.lbl_email.grid(row=2, column=0)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=2, column=1)

        # Botão de Adicionar Contato
        self.btn_adicionar = tk.Button(root, text="Adicionar Contato", command=self.adicionar_contato)
        self.btn_adicionar.grid(row=3, columnspan=2)

        # Botão de Visualizar Contatos
        self.btn_visualizar = tk.Button(root, text="Visualizar Contatos", command=self.visualizar_contatos)
        self.btn_visualizar.grid(row=4, columnspan=2)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        email = self.entry_email.get()

        if not nome or not telefone or not email:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        else:
            self.agenda.adicionar_contato(nome, telefone, email)
            messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")

    def visualizar_contatos(self):
        contatos = self.agenda.visualizar_contatos()
        if not contatos:
            messagebox.showinfo("Contatos", "Nenhum contato encontrado.")
        else:
            contatos_str = "\n".join([f"Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}" for contato in contatos])
            messagebox.showinfo("Contatos", contatos_str)


