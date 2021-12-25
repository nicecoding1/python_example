import random
import time

names = """나이스1
나이스2
나이스3
나이스4
나이스5
나이스6
나이스7
나이스8
나이스9
나이스10
나이스11
나이스12
나이스13
나이스14
나이스15
나이스16
나이스17
나이스18
나이스19
나이스20
나이스21
나이스22
나이스23
나이스24
나이스25"""

arr = names.split("\n")
cnt = len(arr)

lottery_cnt = 5 #추첨 인원
lottery_name = []
for i in range(lottery_cnt):
    random.shuffle(arr)
    random.shuffle(arr)
    random.shuffle(arr)
    for i in range(100):
        print(f"\r{i}", end='')
        time.sleep(0.03)

    s = arr.pop()
    lottery_name.append(s)
    print(f"\r추첨 --> {s}")
    time.sleep(3)

print()
print("*"*20)
print("선물 당첨자 명단")
print("*"*20)
no = 1
for i in lottery_name:
    print(no, ":", i)
    no += 1
