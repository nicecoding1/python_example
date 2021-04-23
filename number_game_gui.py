import tkinter as tk
from tkinter import messagebox
import random

trial = 0
success = False

def callback(event):
    guess()

def guess():
    global random_num, trial, success

    if success:
        tk.messagebox.showerror("확인", "이미 성공하였습니다!")
        return

    my_num = str(num_entry.get())
    if my_num == "":
        tk.messagebox.showerror("확인", "숫자를 입력하세요!")
        num_entry.focus()
        return

    trial += 1
    if random_num == my_num:
        bottom_label['text'] = "(%d번 시도) 성공" % trial
        success_label.grid(row=0, column=0)
        success = True
    elif random_num > my_num:
        bottom_label['text'] = "(%d번 시도) Up" % trial
        num_entry.delete('0', tk.END)
        num_entry.focus()
    elif random_num < my_num:
        bottom_label['text'] = "(%d번 시도) Down" % trial
        num_entry.delete('0', tk.END)
        num_entry.focus()   


window = tk.Tk()
window.title("숫자 맞추기 게임")
window.geometry("500x400")

frame1 = tk.Frame(window, pady="10")
frame1.pack()

frame2 = tk.Frame(window, pady=10)
frame2.pack()

frame3 = tk.Frame(window)
frame3.pack()

frame4 = tk.Frame(window)
frame4.pack()

top_label = tk.Label(frame1, text="1~100 사이의 숫자 하나를 맞추세요", bg="yellow", font="Times 16 bold")
top_label.grid(row=0, column=0)

num_label = tk.Label(frame2, text="숫자 입력 : ", padx=10, pady=10)
num_label.grid(row=0, column=0)
num_entry = tk.Entry(frame2, width="7")
num_entry.grid(row=0, column=1)
num_btn = tk.Button(frame2, text="입력", command=guess)
num_btn.grid(row=0, column=2)

bottom_label = tk.Label(frame3, text="")
bottom_label.grid(row=0, column=0)

success_img = tk.PhotoImage(file="guess_success.png")
success_label = tk.Label(frame4, image=success_img, pady=20)

random_num = str(random.randrange(1, 100))
print(random_num)

num_entry.focus()
num_entry.bind('<Return>', callback)

window.mainloop()
