import tkinter as tk
from gui.main_window import MainWindow
from gui.second_window import SecondWindow
from db.database import init_db

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Applicazione Tkinter con SQLAlchemy")
        self.main_window = None
        self.second_window = None
        self.setup()

    def setup(self):
        init_db()
        self.navigate_to_main_window()

    def navigate_to_main_window(self):
        if self.second_window:
            self.second_window.destroy()
        self.main_window = MainWindow(self.root, self.navigate_to_second_window)
        self.main_window.pack()

    def navigate_to_second_window(self):
        if self.main_window:
            self.main_window.destroy()
        self.second_window = SecondWindow(self.root, self.navigate_to_main_window)
        self.second_window.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
