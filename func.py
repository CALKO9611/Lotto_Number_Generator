from tkinter import *
import random


# 시작 버튼
def lotto_start(list_file, game_combobox):
    list_file.delete(0, END)  # 시작 누르면서 동시에 초기화
    for i in range(int(game_combobox.get())):
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        list_file.insert(END, lotto)
