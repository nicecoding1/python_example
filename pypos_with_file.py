import tkinter as tk
import pickle, os
import datetime as dt

today = dt.datetime.now()
today_str = today.strftime("%Y-%m-%d")

price_meal = {"김밥": 3000, "라면": 3500, "떡볶이": 5000, "튀김": 5000, "쫄면": 7000}
price_drink = {"콜라": 1000, "사이다": 1000, "환타": 1000, "레몬에이드": 3000, "자몽에이드": 3500}
# 결제내역 저장 리스트
paylog = []
# 테이블 정보 딕셔너리
table = {}
# 현재 처리 중인 테이블 번호
table_no = ""

# 테이블 선택
def table_select(tno):
    global table_no
    table_no = tno

    print("table number:", tno)
    label_table.configure(text="테이블 " + str(table_no))

    frame5.pack_forget()
    frame6.pack_forget()
    print_order()
    print_price()
    show_meal()


# 테이블 보여줌
def show_table():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack(fill="both", expand=True)
    frame6.pack_forget()


# 식사 메뉴 보여줌
def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame6.pack_forget()
    frame1.pack(fill="both", expand=True)
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


# 음료 메뉴 보여줌
def show_drink():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="yellow")
    frame4.pack_forget()
    frame2.pack_forget()
    frame6.pack_forget()
    frame1.pack(fill="both", expand=True)
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


# 식사 주문
def meal_add(m):
    global price_meal, table, table_no, today_str

    order_meal = table[table_no][0]
    total_price = table[table_no][2]

    if m not in price_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_meal.get(m)
    total_price += this_price

    if m in order_meal:
        order_meal[m] = order_meal.get(m) + 1
    else:
        order_meal[m] = 1

    table[table_no][0] = order_meal
    table[table_no][2] = total_price
    table[table_no][3] = today_str

    print_order()
    print_price()
    
    for i in table:
        print(table[i])
    print()


# 음료 주문
def drink_add(m):
    global price_drink, table, table_no
    order_drink = table[table_no][1]
    total_price = table[table_no][2]

    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1

    table[table_no][1] = order_drink
    table[table_no][2] = total_price
    table[table_no][3] = today_str

    print_order()
    print_price()
    
    for i in table:
        print(table[i])
    print()


# 주문내역 화면 출력
def print_order():
    global table, table_no

    order_meal = table[table_no][0]
    order_drink = table[table_no][1]

    tmp = ""
    price_tmp = 0
    for i in order_meal:
        price_tmp = price_meal[i] * order_meal.get(i)
        tmp = tmp + i + " X " + str(order_meal.get(i)) +  " = " + str(price_tmp)+"\n"
    for i in order_drink:
        price_tmp = price_drink[i] * order_drink.get(i)
        tmp = tmp + i + " X " + str(order_drink.get(i)) +  " = " + str(price_tmp)+"\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)


# 주문 완료
def order_end():
    global table_no
    table_no = ""

    show_table()
    

# 상단 금액 출력
def print_price():
    global table, table_no
    total_price = table[table_no][2]
    label_price.configure(text=str(total_price)+" 원")


# 금액 계산
def cal_pay(event):
    global table, table_no
    total_price = table[table_no][2]
    label_price.configure(text=str(total_price)+" 원")
    label_total2.configure(text=str(total_price)+" 원")
    test = str(entry_pay.get())
    if test == "":
        pay = 0
    else:
        pay = int(test)

    if pay > total_price:
        jan = pay - total_price
        label_jan2.configure(text=str(jan)+" 원")
    else:
        label_jan2.configure(text="0 원")
    

# 결제    
def pay():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack(fill="both", expand=True)
    cal_pay('')


# 결제 완료
def pay_end():
    global table, table_no, paylog, entry_pay
    paylog.append(table[table_no])

    with open("pypos.pickle", "wb") as f:
        pickle.dump(paylog, f)

    table[table_no] = [{}, {}, 0, today_str, table_no]
    table_no = ""
    entry_pay.delete('0', tk.END)
    frame6.pack_forget()
    show_table()
    today_result()
    

# 당일 매출 출력
def today_result():
    global paylog, today_str
    result = 0
    for i in paylog:
        if i[3] == today_str:
            result += i[2]
    print("{} 매출 실적: {}원".format(today_str, result))
    

if os.path.exists("pypos.pickle"):
    with open("pypos.pickle", "rb") as f:
        paylog = pickle.load(f)
    
    for row in paylog:
        print(row)


window = tk.Tk()
window.title("PyPOS Ver 0.1")
window.geometry("600x400+500+300")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10")
# frame1.pack(fill="both")

frame5 = tk.Frame(window, width="600", height="10")
frame5.pack(fill="both", expand=True)

frame2 = tk.Frame(window, width="600")
# frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(window, width="600")
# frame3.pack(fill="both", expand=True)

frame4 = tk.Frame(window, width="600", height="10")
# frame4.pack(fill="both", expand=True)

frame6 = tk.Frame(window, width="600")
# frame6.pack(fill="both", expand=True)


label_table = tk.Label(frame1, text="테이블번호 ", padx=10, pady=10, fg="red", font='Arial 15')
label_table.grid(row=0, column=0, padx=10, pady=10)

btn_meal = tk.Button(frame1, text="식사", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=1, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="음료", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=2, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문종료", padx="10", pady="10", command=order_end)
btn_end.grid(row=0, column=3, padx=10, pady=10)

btn_pay = tk.Button(frame1, text="결제", padx="10", pady="10", command=pay)
btn_pay.grid(row=0, column=4, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="10", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column=5, padx="10", pady="10")

# 식사
btn_meal_1 = tk.Button(frame2, text="김밥\n(3000원)", padx="10", pady="10", width="10", command=lambda: meal_add('김밥'))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = tk.Button(frame2, text="라면\n(3500원)", padx="10", pady="10", width="10", command=lambda: meal_add('라면'))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = tk.Button(frame2, text="떡볶이\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('떡볶이'))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = tk.Button(frame2, text="튀김\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('튀김'))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = tk.Button(frame2, text="쫄면\n(7000원)", padx="10", pady="10", width="10", command=lambda: meal_add('쫄면'))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)


# 음료
btn_drink_1 = tk.Button(frame3, text="콜라\n(1000원)", padx="10", pady="10", width="10", command=lambda: drink_add('콜라'))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

btn_drink_2 = tk.Button(frame3, text="사이다\n(1000원)", padx="10", pady="10", width="10", command=lambda: drink_add('사이다'))
btn_drink_2.grid(row=0, column=1, padx=10, pady=10)

btn_drink_3 = tk.Button(frame3, text="환타\n(1000원)", padx="10", pady="10", width="10", command=lambda: drink_add('환타'))
btn_drink_3.grid(row=0, column=2, padx=10, pady=10)

btn_drink_4 = tk.Button(frame3, text="레몬에이드\n(3000원)", padx="10", pady="10", width="10", command=lambda: drink_add('레몬에이드'))
btn_drink_4.grid(row=0, column=3, padx=10, pady=10)

btn_drink_5 = tk.Button(frame3, text="자몽에이드\n(3500원)", padx="10", pady="10", width="10", command=lambda: drink_add('자몽에이드'))
btn_drink_5.grid(row=0, column=4, padx=10, pady=10)

# 테이블
btn_table_1 = tk.Button(frame5, text="테이블 1", padx="10", pady="10", width="10", command=lambda: table_select(1))
btn_table_1.grid(row=0, column=0, padx=20, pady=20)

btn_table_2 = tk.Button(frame5, text="테이블 2", padx="10", pady="10", width="10", command=lambda: table_select(2))
btn_table_2.grid(row=0, column=1, padx=20, pady=20)

btn_table_3 = tk.Button(frame5, text="테이블 3", padx="10", pady="10", width="10", command=lambda: table_select(3))
btn_table_3.grid(row=0, column=2, padx=20, pady=20)

btn_table_4 = tk.Button(frame5, text="테이블 4", padx="10", pady="10", width="10", command=lambda: table_select(4))
btn_table_4.grid(row=0, column=3, padx=20, pady=20)

btn_table_5 = tk.Button(frame5, text="테이블 5", padx="10", pady="10", width="10", command=lambda: table_select(5))
btn_table_5.grid(row=1, column=0, padx=20, pady=20)

btn_table_6 = tk.Button(frame5, text="테이블 6", padx="10", pady="10", width="10", command=lambda: table_select(6))
btn_table_6.grid(row=1, column=1, padx=20, pady=20)

btn_table_7 = tk.Button(frame5, text="테이블 7", padx="10", pady="10", width="10", command=lambda: table_select(7))
btn_table_7.grid(row=1, column=2, padx=20, pady=20)

btn_table_8 = tk.Button(frame5, text="테이블 8", padx="10", pady="10", width="10", command=lambda: table_select(8))
btn_table_8.grid(row=1, column=3, padx=20, pady=20)

# 주문 리스트
text_1 = tk.Text(frame4, height="10")
text_1.pack()

# 결제(금액, 내신돈, 받으실돈)
label_total = tk.Label(frame6, text="결제금액", padx=10, pady="3", font='Arial 15')
label_total.grid(row=0, column=0, padx="10", pady="3")

label_total2 = tk.Label(frame6, text="0원", padx=10, pady="3", font='Arial 15')
label_total2.grid(row=0, column=1, padx="10", pady="3")

label_pay = tk.Label(frame6, text="내신돈", padx=10, pady="3", font='Arial 15')
label_pay.grid(row=1, column=0, padx="10", pady="3")

entry_pay=tk.Entry(frame6, width=10, font='Arial 15')
entry_pay.insert('0', "")
entry_pay.bind("<Return>", cal_pay)
entry_pay.grid(row=1, column=1, padx="10", pady="3")

label_jan = tk.Label(frame6, text="받으실돈", padx=10, pady="3", font='Arial 15')
label_jan.grid(row=2, column=0, padx="10", pady="3")

label_jan2 = tk.Label(frame6, text="0원", padx=10, pady="10", font='Arial 15')
label_jan2.grid(row=2, column=1, padx="10", pady="3")

btn_payend = tk.Button(frame6, text="결제 완료", padx="10", pady="10", command=pay_end)
btn_payend.grid(row=3, column=0, padx=10, pady=10)


# 테이블 세팅
for i in range(1, 9):
    table[i] = [{}, {}, 0, today_str, i]

window.mainloop()