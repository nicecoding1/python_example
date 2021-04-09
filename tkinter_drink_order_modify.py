import tkinter as tk
from tkinter import messagebox
from openpyxl import load_workbook
from datetime import datetime

price = {'coffee': 3500, 'latte': 4000, 'smoothie': 4500, 'tea': 3000}
order = []
order2 = {'coffee': 0, 'latte': 0, 'smoothie': 0, 'tea': 0}
sum = 0


def clear():
    global sum, order, order2, textarea, entry1, entry2
    textarea.delete('1.0', tk.END)
    label1['text'] = "금액: 0원"
    sum = 0
    order = []
    order2 = {'coffee': 0, 'latte': 0, 'smoothie': 0, 'tea': 0}
    entry1.delete('0', tk.END)
    entry2.delete('0', tk.END)
    entry1.focus()

def add(item):
    global sum

    if item not in price:
        print("no drink")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    order2[item] += 1
    textarea.insert(tk.INSERT, item+" ")
    label1['text'] = "금액: " + str(sum) + "원"

def send():
    global order, order2, sum, entry1, entry2
    name = str(entry1.get())
    hp = str(entry2.get())
    print(name, hp)
    print(order)
    print(order2)

    now_dt = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    wb = load_workbook("drink_order.xlsx")
    ws = wb['Sheet1']
    ws.append([now_dt, name, hp, order2['coffee'], order2['latte'], order2['smoothie'], order2['tea'], sum])
    wb.save("drink_order.xlsx")

    clear()


def btn_exit():
    name = str(entry1.get())
    hp = str(entry2.get())

    if name == "":
        tk.messagebox.showerror("확인", "이름을 입력해주세요!")
        entry1.focus()
        return
    if hp == "":
        tk.messagebox.showerror("확인", "휴대폰번호를 입력해주세요!")
        entry2.focus()
        return

    msgbox = tk.messagebox.askquestion('확인', '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        send()


window = tk.Tk()
window.title("음료 주문")
window.geometry("450x550")

frame1 = tk.Frame(window)
frame1.pack()

btn_1 = tk.Button(frame1, text="커피", command=lambda: add('coffee'), width=10, height=2)
btn_2 = tk.Button(frame1, text="라떼", command=lambda: add('latte'), width=10, height=2)
btn_3 = tk.Button(frame1, text="스무디", command=lambda: add('smoothie'), width=10, height=2)
btn_4 = tk.Button(frame1, text="차", command=lambda: add('tea'), width=10, height=2)
btn_5 = tk.Button(frame1, text="주문완료", command=btn_exit, width=10, height=2)

btn_1.grid(row=0, column=0, padx=10, pady=10)
btn_2.grid(row=0, column=1, padx=10, pady=10)
btn_3.grid(row=0, column=2, padx=10, pady=10)
btn_4.grid(row=0, column=3, padx=10, pady=10)
btn_5.grid(row=1, column=0, padx=10, pady=10)

frame2 = tk.Frame(window)
frame2.pack()

label2 = tk.Label(frame2, text="이름", width=10, height=2).grid(row=0, column=0)
label3 = tk.Label(frame2, text="휴대폰번호", width=10, height=2).grid(row=1, column=0)

entry1 = tk.Entry(frame2)
entry2 = tk.Entry(frame2)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

label1 = tk.Label(window, text="금액: 0원", width=100, height=2, fg="blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack(padx=10, pady=10)

window.mainloop()