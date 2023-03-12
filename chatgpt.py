#chatgpt가 준 코드
import tkinter as tk
import time

root = tk.Tk()
root.title("시계")

current_time = time.strftime("%H:%M:%S")

clock_label = tk.Label(root, text=current_time, font=("Helvetica", 48))
clock_label.pack(pady=20)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)

update_time()
root.mainloop()
