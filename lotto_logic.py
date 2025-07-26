from tkinter import *
import tkinter.messagebox as msgbox
import random
import webbrowser
import requests


# 최근 당첨 번호 불러오기
def fetch_recent_lotto():
    try:
        recent_draw = 1181  # 최근 회차 번호 로직 추가해야함
        url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={recent_draw}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["returnValue"] == "success":
            numbers = [
                data["drwtNo1"],
                data["drwtNo2"],
                data["drwtNo3"],
                data["drwtNo4"],
                data["drwtNo5"],
                data["drwtNo6"],
            ]
            bonus = data["bnusNo"]
            draw_date = data["drwNoDate"]

            return (
                f"로또 {recent_draw}회차 당첨 번호 ({draw_date})\n"
                f"{', '.join(map(str, numbers))} + 보너스 {bonus}"
            )

        else:
            return {"error": "API 요청 실패"}

    except Exception as e:
        return {"error": str(e)}


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
