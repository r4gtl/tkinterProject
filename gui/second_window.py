import tkinter as tk
from tkinter import ttk
from db.models import SessionLocal, Utente

class SecondWindow(tk.Frame):
    def __init__(self, master, navigate_back):
        super().__init__(master)
        self.master = master
        self.navigate_back = navigate_back

        self.label = ttk.Label(self, text="Inserisci un nuovo utente")
        self.label.pack(pady=10)

        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, "Nome")

        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, "Email")

        self.submit_button = ttk.Button(self, text="Salva", command=self.save_user)
        self.submit_button.pack(pady=5)

        self.back_button = ttk.Button(self, text="Indietro", command=self.navigate_back)
        self.back_button.pack(pady=10)

        self.session = SessionLocal()

    def save_user(self):
        nome = self.name_entry.get()
        email = self.email_entry.get()
        new_user = Utente(nome=nome, email=email)
        self.session.add(new_user)
        self.session.commit()

    def destroy(self):
        self.session.close()
        super().destroy()
