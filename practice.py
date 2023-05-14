import pyautogui as auto
import pyperclip as clip
from time import sleep


def set_page(link):
    auto.hotkey("win", "r", interval=0.1)
    auto.write(link)
    auto.press("return", interval=0.5)

set_page("https://naver.com") # 네이버 접속
value = auto.prompt("검색어를 입력해주세요", "검색어 입력")
clip.copy(value)  # 값 복사
auto.hotkey("ctrl", "v", interval=0.5)  # 붙여넣기
auto.press("return", interval=0.1)
