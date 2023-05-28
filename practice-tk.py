from tkinter import *
from tkinter import filedialog
import os
app = Tk()
app.title("메모장")
app.geometry('500x400')

ROOT_FILE_DIR = ""
FONT_SIZE = 14
FONT = "Arial {}"
# 함수 선언부


def save():
    global ROOT_FILE_DIR
    if ROOT_FILE_DIR != "":
        with open(ROOT_FILE_DIR, "w", encoding="utf-8") as w:
            f = text.get("1.0", END).rstrip()
            w.write(f)
    else:
        save_absolute()


def save_absolute():
    global ROOT_FILE_DIR
    rootdir = os.path.abspath(os.path.dirname(__file__))
    filename = filedialog.asksaveasfilename(
        title="save file",
        initialdir=rootdir, filetypes=(("text file", "*.txt"),))
    if not filename.endswith(".txt"):
        filename += ".txt"
    ROOT_FILE_DIR = filename
    save()


def load():
    global ROOT_FILE_DIR
    rootdir = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")
    filename = filedialog.askopenfilename(
        initialdir=rootdir, title="open file", filetypes=(("text file", "*.txt"), ))
    with open(filename, "r", encoding="utf-8") as r:
        f = r.read()
        text.delete("1.0", END)
        text.insert("1.0", f)
    ROOT_FILE_DIR = filename


def clear():
    text.delete("1.0", END)


def font_plus():
    global FONT_SIZE
    FONT_SIZE = FONT_SIZE+5
    text.configure(font=FONT.format(FONT_SIZE))


def font_minus():
    global FONT_SIZE
    FONT_SIZE = FONT_SIZE-5
    if FONT_SIZE <= 0:
        FONT_SIZE = 5
    text.configure(font=FONT.format(FONT_SIZE))


menu = Menu(app)
file = Menu(menu, tearoff=0)
file.add_command(label="저장", command=save, accelerator="Command+S")
file.add_command(label="다른 이름으로 저장", command=save_absolute,
                 accelerator="Command+Shift+S")
file.add_command(label="불러오기", command=load, accelerator="Command+O")
file.add_command(label="모두삭제", command=clear, accelerator="Command+X")
menu.add_cascade(label="파일", menu=file)

setting = Menu(menu, tearoff=0)
setting.add_command(label="글자 키우기", command=font_plus,
                    accelerator="Command++")
setting.add_command(label="글자 줄이기", command=font_minus,
                    accelerator="Command+-")
menu.add_cascade(label="설정", menu=setting)

text = Text(app, font=FONT.format(FONT_SIZE))
text.pack(expand=True, fill=BOTH)

app.config(menu=menu)
app.mainloop()
