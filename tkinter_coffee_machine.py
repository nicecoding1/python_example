import tkinter as tk
from tkinter import messagebox

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def add():
    global c1Var, c2Var, c3Var, c4Var
    sum = 0
    order = ""

    if c1Var.get() == 1:
        sum += 3000
        order += "아메리카노/"
    if c2Var.get() == 1:
        sum += 4000
        order += "카페라떼/"
    if c3Var.get() == 1:
        sum += 4000
        order += "카프치노/"
    if c4Var.get() == 1:
        sum += 5000
        order += "에스프레소/"
    label1['text'] = "금액: " + str(sum) + "원"
    label2['text'] = "선택: " + order


def btn_exit():
    msgbox = tk.messagebox.askquestion('확인','주문을 마치시겠습니까?')
    if msgbox == 'yes':
        exit()


window = tk.Tk()
window.title("커피자판기")
window.geometry("300x400")
# center(window)

frame1 = tk.Frame(window)
frame1.pack()
tk.Label(window, text="커피자판기")

label0 = tk.Label(window, text="커피자판기", width=100, height=2, font="Arial 15")
label0.pack()

c1Var = tk.IntVar()
c2Var = tk.IntVar()
c3Var = tk.IntVar()
c4Var = tk.IntVar()

c1 = tk.Checkbutton(window, text="아메리카노        -  3000원", variable=c1Var, command=add)
c2 = tk.Checkbutton(window, text="카페라떼          -  4000원", variable=c2Var, command=add)
c3 = tk.Checkbutton(window, text="카프치노          -  4000원", variable=c3Var, command=add)
c4 = tk.Checkbutton(window, text="에스프레소        -  5000원", variable=c4Var, command=add)

c1.pack()
c2.pack()
c3.pack()
c4.pack()

label1 = tk.Label(window, text="금액: 0원", width=100, height=2, pady="20")
label1.pack()

label2 = tk.Label(window, text="선택음료", width=100, height=2)
label2.pack()

window.mainloop()
