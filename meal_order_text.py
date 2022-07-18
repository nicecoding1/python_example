import os

menu_list = []
menu_dic = {}
order_list = []
order_price = 0

def print_menu():
    print("="*30)
    if len(order_list):
        print("주문한 메뉴: {}".format(order_list))
        print()
    print("[주문 가능 메뉴]")
    for i in menu_dic:
        print("{} - {}원".format(i, menu_dic[i]))

    menu = input("주문할 음식명을 입력해주세요(종료: 0): ")
    while menu not in menu_dic and menu != "0":
        print(menu,"은(는) 주문 가능 메뉴에 없습니다")
        menu = input("주문할 음식명을 입력해주세요(종료: 0): ")
    return menu


def print_order():
    if len(order_list) < 1:
        print("주문 내역이 없습니다.")
        exit()
    print("주문한 메뉴: {}".format(",".join(order_list)))


def print_price():
    print("금액: {}원".format(order_price))


def print_change(c):
    print("잔돈: {}원".format(c))


if os.path.exists("meal_menu.txt"):
    with open("meal_menu.txt", "r", encoding="utf-8") as f:
        menu_list = f.readlines()

for i in menu_list:
    name = i.strip().split(",")[0]
    price = i.strip().split(",")[1]

    menu_dic[name] = int(price)


menu = ""
while menu != "0":
    menu = print_menu()
    if menu == "0":
        break
    price = menu_dic[menu]
    order_list.append(menu)
    order_price += price


print_order()
print_price()

pay = int(input("손님에게 받은 금액을 입력하세요(숫자만): "))
change = pay - order_price

print_change(change)
