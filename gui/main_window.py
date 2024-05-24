import tkinter as tk
from tkinter import ttk
from db.models import SessionLocal, Utente

class MainWindow(tk.Frame):
    def __init__(self, master, navigate_to_second_window):
        super().__init__(master)
        self.master = master
        self.navigate_to_second_window = navigate_to_second_window

        self.label = ttk.Label(self, text="Benvenuto!")
        self.label.pack(pady=10)

        self.button = ttk.Button(self, text="Vai alla Seconda Finestra", command=self.navigate_to_second_window)
        self.button.pack(pady=10)

        self.session = SessionLocal()
        self.display_users()

    def display_users(self):
        users = self.session.query(Utente).all()
        for user in users:
            self.label = ttk.Label(self, text=f"Utente: {user.nome}, Email: {user.email}")
            self.label.pack()

    def destroy(self):
        self.session.close()
        super().destroy()
