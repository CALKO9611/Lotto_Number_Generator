from tkinter import *


def setup_ui(root):
    # 소개 문구 프레임
    intro_frame = Frame(root)
    intro_frame.pack(fill="both")

    intro_label = Label(
        intro_frame,
        text="로또 번호 자동 추출 프로그램입니다.\n사용 방법은 '도움말' 버튼을 눌러 확인해주세요.",
    )
    intro_label.pack()

    # 리스트 프레임
    list_frame = Frame(root)
    list_frame.pack(side="left", fill="both", padx=5, pady=5)

    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    list_file = Listbox(
        list_frame,
        selectmode="extended",
        width=30,
        height=10,
        yscrollcommand=scrollbar.set,
    )
    list_file.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=list_file.yview)
