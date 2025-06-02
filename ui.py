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
