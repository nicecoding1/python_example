import random
import time
import pickle
import os.path


def print_program_name():
    print()
    print("*"*30)
    print(" 선물 추첨 프로그램 Ver 0.1")
    print("*"*30)


def save_result(result):
    with open("gift_lottery_result.txt", "a+", encoding="utf8") as f:
        f.write(result+"\n")


def clear_result():
    with open("gift_lottery_result.txt", "w+", encoding="utf8") as f:
        f.write("")


def save_names(names):
    with open("gift_lottery.pickle", "wb") as f:
        pickle.dump(names, f)


print_program_name()

if os.path.exists("gift_lottery.pickle"):
    with open("gift_lottery.pickle", "rb") as f:
        arr = pickle.load(f)
else:
    arr = []

lottery_name = []

while True:
    menu = input("\n메뉴 선택(1.추첨 2.결과 조회 3.결과 삭제 4.이름 초기화 5.이름 출력 6.이름추가 9.종료): ")
    if menu == "1":
        gift = input("선물 이름을 입력하세요: ")
        inwon = int(input("추첨 인원을 입력하세요: "))
        lottery_cnt = inwon #추첨 인원
        
        for i in range(lottery_cnt):
            random.shuffle(arr)
            random.shuffle(arr)
            random.shuffle(arr)
            for i in range(0,100,2):
                print(f"\r{i}", end='')
                time.sleep(0.05)

            s = arr.pop()
            lottery_name.append([gift,s])
            save_result("{} - {}".format(gift, s))
            print(f"\r추첨 --> {s}")
            time.sleep(2)

        print()
        print("*"*20)
        print(" 선물 당첨자 명단")
        print("*"*20)
        no = 1
        for i in lottery_name:
            print(no, ":", i)
            no += 1

    elif menu == "2":
        print()
        print("*"*20)
        print(" 선물 당첨자 명단")
        print("*"*20)
        no = 1
        for i in lottery_name:
            print(no, ":", i)
            no += 1

    elif menu == "3":
        lottery_name = []
        clear_result()

    elif menu == "4":
        arr = []

    elif menu == "5":
        print(arr)        

    elif menu == "6":
        tmp = input("추가할 이름을 입력하세요(,으로 구분): ")
        names = tmp.split(",")
        arr.extend(names)
        print(names,"을 추가하였습니다.")

    elif menu == "9":
        save_names(arr)
        print("프로그램이 종료되었습니다!")
        break
