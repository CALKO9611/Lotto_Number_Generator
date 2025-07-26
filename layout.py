from tkinter import *
from tkinter import font
from lotto_logic import *
import tkinter.ttk as ttk


def setup_main_ui(root):
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

    # 폰트 객체를 상황별로 정의
    bold_font_10 = font.Font(family=selected_font, weight="bold", size=10)
    normal_font_10 = font.Font(family=selected_font, size=10)
    normal_font_12 = font.Font(family=selected_font, size=12)

    # 소개 문구 프레임
    intro_frame = Frame(root, relief="groove", bd=3)
    intro_frame.pack(fill="both")

    intro_label = Label(
        intro_frame,
        text="로또 번호 자동 추출 프로그램입니다.\n사용 방법은 '도움말' 버튼을 눌러 확인해주세요.",
        padx=5,
        pady=5,
        font=bold_font_10,
    )
    intro_label.pack()

    # 최근 당첨 번호 라벨
    recent_numbers = fetch_recent_lotto()

    if isinstance(recent_numbers, dict) and "error" in recent_numbers:
        error_msg = f"오류 발생:\n{recent_numbers['error']}"
        recent_numbers_label = Label(
            intro_frame,
            text=error_msg,
            padx=5,
            pady=5,
            font=normal_font_10,
            fg="red",
        )
    else:
        recent_numbers_label = Label(
            intro_frame,
            text=recent_numbers,
            padx=5,
            pady=5,
            font=normal_font_10,
            fg="blue",
        )
    recent_numbers_label.pack()

    # 리스트 프레임
    list_frame = Frame(root)
    list_frame.pack(side="left", fill="both", padx=5, pady=5)

    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    list_file = Listbox(
        list_frame,
        selectmode="extended",
        font=normal_font_12,
        yscrollcommand=scrollbar.set,
    )
    list_file.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=list_file.yview)

    # 실행 프레임
    frame_run = Frame(root)
    frame_run.pack(fill="both", padx=5, pady=5)

    # 게임 수 선택 라벨 프레임
    game_count = LabelFrame(frame_run, text="게임 수", font=bold_font_10)
    game_count.pack(padx=5, pady=5)

    game_values = [5, 10, 50]
    game_combobox = ttk.Combobox(
        game_count,
        width=8,
        height=2,
        values=game_values,
        font=normal_font_10,
        state="readonly",
    )
    game_combobox.current(0)
    game_combobox.pack()

    # 버튼
    start_Button = Button(
        frame_run,
        text="시작",
        width=10,
        height=2,
        font=normal_font_10,
        command=lambda: handle_start_button(list_file, game_combobox),
    )
    start_Button.pack(padx=3, pady=3)

    help_Button = Button(
        frame_run,
        text="도움말",
        width=10,
        height=2,
        font=normal_font_10,
        command=show_help_message,
    )
    help_Button.pack(padx=3, pady=3)

    dhlottery_Button = Button(
        frame_run,
        text="동행복권\n사이트",
        width=10,
        height=2,
        font=normal_font_10,
        command=lambda: open_lotto_site("https://www.dhlottery.co.kr/"),
    )
    dhlottery_Button.pack(padx=3, pady=3)

    end_Button = Button(
        frame_run,
        text="종료",
        width=10,
        height=2,
        font=normal_font_10,
        command=root.quit,
    )
    end_Button.pack(padx=3, pady=3)
