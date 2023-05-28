from tkinter import *

FONT = "Arial {}"
W = 3
H = 2

# 창 기본설정
app = Tk()
app.title('계산기')
app.minsize(width=350, height=500)  # 창의 최소크기를 350x500으로 지정

# 입력 라벨
input_label = Label(app, text="", font=FONT.format(20),
                    background='#FFFFFF', height=2)
input_label.pack(fill=BOTH)

# 결과 라벨
result_label = Label(app, text="", font=FONT.format(
    15), background='#FFFFFF', height=2, borderwidth=1, relief='solid')
result_label.pack(fill=BOTH)

# 키패드 프레임
frame = Frame(app)
frame.pack()

# 버튼은 frame영역에서 작업한다.
for row in range(3):       # 행
    for col in range(3):   # 열
        cnt = row*3+col+1  # 행이 증가할 때마다 3을 증가시켜줌
        btn = Button(frame, text=cnt, width=W, height=H, font=FONT.format(
            20))
        btn.grid(row=row, column=col)
btn0 = Button(frame, text="0", width=W, height=H,
              font=FONT.format(20))
btn0.grid(row=3, column=1)

app.mainloop()
