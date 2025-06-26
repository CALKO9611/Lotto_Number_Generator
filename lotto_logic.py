from tkinter import *
import tkinter.messagebox as msgbox
import random
import webbrowser


# 로또 번호 생성 함수
def generate_lotto_numbers():
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    return lotto


# 시작 버튼
def handle_start_button(list_file, game_combobox):
    list_file.delete(0, END)  # 시작 누르면서 동시에 초기화
    for i in range(int(game_combobox.get())):
        lotto_num = generate_lotto_numbers()
        list_file.insert(END, lotto_num)


# 도움말 버튼
def show_help_message():
    msgbox.showinfo(
        "도움말",
        "[프로그램 사용 방법]\n1. '게임 수'를 설정 후 '시작' 버튼을 누르세요.\n2. '동행복권 사이트' 버튼을 누르면 \nhttps://www.dhlottery.co.kr/ 로 연결됩니다.\n\n당첨을 기원합니다! (*＾▽＾)／\n\nDeveloped by CALKO",
    )


# 동행복권 사이트 버튼
def open_lotto_site(url):
    webbrowser.open_new(url)
