from tkinter import *

window=Tk()
window.title("그림판")
window.geometry("640x400")

color=["red","yellow","green","blue","white","black","cyan","magenta"]
color_lb=Listbox(window)
for i, c_name in enumerate(color):
    color_lb.insert(i, c_name)
color_lb.pack()

def apply():
    window.config(bg=color_lb.get(color_lb.curselection()))

bg_btn=Button(window, text="적용", width=3, height=1)
bg_btn.pack()

window.mainloop()