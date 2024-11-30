import pyautogui as auto
import pyperclip as clip
from time import sleep

def set_page(link):
    auto.hotkey("win", "r", interval=0.2)
    auto.write(link, interval=0.1)
    auto.press("return", interval=0.1)
    auto.hotkey("win", "m", interval=0.1)

user_id = auto.prompt("아이디를 입력해주세요", "아이디 입력")
passwd = auto.password("패스워드를 입력해주세요", "패스워드 입력", mask="*")

set_page("https://nid.naver.com/nidlogin.login")  # 로그인 페이지
auto.click()
auto.write(user_id, interval=0.1)  # 입력 인터벌 0.1초
auto.press("tab", interval=0.1)  # 비밀번호 선택
auto.write(passwd, interval=0.1)  # 입력 인터벌 0.1초
auto.press("return", interval=0.1)
