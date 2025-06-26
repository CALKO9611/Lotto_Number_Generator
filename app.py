import tkinter as tk
from layout import setup_main_ui

root = tk.Tk()
root.title("로또 번호 생성기")
root.resizable(False, False)

# ui
setup_main_ui(root)

root.mainloop()
