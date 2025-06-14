from tkinter import *
from tkinter import font
from func import lotto_start
import tkinter.ttk as ttk


def setup_ui(root):
    # 폰트
    preferred_fonts = [
        "맑은 고딕",
        "Segoe UI",
        "Arial",
        "AppleGothic",
        "Noto Sans CJK KR",
    ]
    for f in preferred_fonts:
        if f in font.families():
            selected_font = f
            break
    else:
        selected_font = "TkDefaultFont"

    bold_font = font.Font(family=selected_font, weight="bold")
    normal_font = font.Font(family=selected_font)

    # 소개 문구 프레임
    intro_frame = Frame(root)
    intro_frame.pack(fill="both")

    intro_label = Label(
        intro_frame,
        text="로또 번호 자동 추출 프로그램입니다.\n사용 방법은 '도움말' 버튼을 눌러 확인해주세요.",
        font=bold_font,
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

    # 실행 프레임
    frame_run = Frame(root)
    frame_run.pack(fill="both", padx=5, pady=5)

    # 게임 수 선택 라벨 프레임
    game_count = LabelFrame(frame_run, text="게임 수")
    game_count.pack(padx=5, pady=5)

    game_values = [5, 10]
    game_combobox = ttk.Combobox(
        game_count, width=10, height=2, values=game_values, state="readonly"
    )
    game_combobox.current(0)
    game_combobox.pack()

    # 버튼
    start_Button = Button(
        frame_run,
        text="시작",
        width=10,
        height=2,
        font=normal_font,
        command=lambda: lotto_start(list_file, game_combobox),
    )
    start_Button.pack(padx=3, pady=3)

    help_Button = Button(frame_run, text="도움말", width=10, height=2, font=normal_font)
    help_Button.pack(padx=3, pady=3)

    dhlottery_Button = Button(
        frame_run, text="동행복권\n사이트", width=10, height=2, font=normal_font
    )
    dhlottery_Button.pack(padx=3, pady=3)

    end_Button = Button(frame_run, text="종료", width=10, height=2, font=normal_font)
    end_Button.pack(padx=3, pady=3)
