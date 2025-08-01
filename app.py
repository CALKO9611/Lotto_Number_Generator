import tkinter as tk
import sys
import os
from layout import setup_main_ui

root = tk.Tk()
root.title("로또 번호 생성기 v1.0")
root.resizable(False, False)

# 아이콘 경로 설정
if getattr(sys, "frozen", False):
    # exe로 실행될 때
    base_path = sys._MEIPASS
else:
    # python으로 실행할 때
    base_path = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(base_path, "icon32.ico")
root.iconbitmap(icon_path)

# ui
setup_main_ui(root)

root.mainloop()
