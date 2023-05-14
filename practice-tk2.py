from tkinter import *
from tkinter import filedialog
import os

app = Tk()
app.title("메모장")
app.geometry("600x400")
app.resizable(True,True)

def save():
    global ROOT_FILE_DIR
    if ROOT_FILE_DIR != "":
        with open(ROOT_FILE_DIR, "w", encoding="utf-8") as w:
            f = text.get("1.0", END)[:-1]
            f = "".join(chr(ord(i) + len(f)) for i in f)
            w.write(f)
    else:
        save_absolute()

def load():
    global ROOT_FILE_DIR
    rootdir = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")
    filename = filedialog.askopenfilename(
        initialdir=rootdir, title="open file", filetypes=(("text file", "*.jcd"), ))
    with open(filename, "r", encoding="utf-8") as r:
        f = r.read()
        f = "".join(chr(ord(i) - len(f)) for i in f)
        text.delete("1.0", END)
        text.insert("1.0", f)
    ROOT_FILE_DIR = filename

def save_absolute():
    global ROOT_FILE_DIR
    rootdir = os.path.abspath(os.path.dirname(__file__))
    filename = filedialog.asksaveasfilename(
        title="save file",
        initialdir=rootdir, filetypes=(("text file", "*.jcd"),))
    if not filename.endswith(".jcd"):
        filename += ".jcd"
    ROOT_FILE_DIR = filename
    save()

def clear():
    text.delete("1.0",END)

def memo_info():
    info=Tk()
    info.title("메모장 정보")
    info.geometry("200x130")
    label_info = info.label(info, text="파이썬 메모장 테스트", font=("Arial", 18))
    label_info.place()
    info.mainloop()

def os_info():
    pass

menu = Menu(app)
file = Menu(menu, tearoff=0)
file.add_command(label="저장", command=save, accelerator="Command+S")
file.add_command(label="다른 이름으로 저장", command=save_absolute,
                 accelerator="Command+Shift+S")
file.add_command(label="불러오기", command=load, accelerator="Command+O")
file.add_command(label="모두삭제", command=clear, accelerator="Command+D")
menu.add_cascade(label="파일", menu=file)

info = Menu(menu, tearoff=0)
info.add_command(label="메모장 정보", command=memo_info)
info.add_command(label="OS 정보", command=os_info)
menu.add_cascade(label="정보", menu=info)

text = Text(app, font="Arial 22")

text.pack(expand=True, fill=BOTH)

app.config(menu=menu)
app.mainloop()
