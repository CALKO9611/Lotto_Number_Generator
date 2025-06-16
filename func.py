from tkinter import *
import tkinter.messagebox as msgbox
import random


# 시작 버튼
def lotto_start(list_file, game_combobox):
    list_file.delete(0, END)  # 시작 누르면서 동시에 초기화
    for i in range(int(game_combobox.get())):
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        list_file.insert(END, lotto)


# 도움말 버튼
def lotto_help():
    msgbox.showinfo(
        "도움말",
        "[프로그램 사용 방법]\n1. '게임 수'를 설정 후 '시작' 버튼을 누르세요.\n2. '동행복권 사이트' 버튼을 누르면 \nhttps://www.dhlottery.co.kr/ 로 연결됩니다.\n\n당첨을 기원합니다! (*＾▽＾)／\n\nDeveloped by CALKO",
    )
