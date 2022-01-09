
"""
[
['홍길동','010-1234-5678'],
['김철수','010-1234-5678'],
['김대한','010-1111-2222']    
]
"""

phonebook = []

print("파이썬 전화번호부 Ver 1.0")
print()

while True:
    print("="*50)
    print("1. 조회, 2. 입력, 3. 수정, 4. 삭제, 5. 종료")
    print("="*50)

    m = input("기능을 선택하세요.(1~5 입력) ").strip()
    if m == "": continue

    if m == "1":# 조회
        print("1. 조회")
        a = input("조회할 이름 또는 전화번호를 입력하세요: ").strip()
        idx = 0
        for i in phonebook:
            if a == "":
                print("[{}] {} {}".format(idx+1, i[0], i[1]))
                idx += 1
            elif a in i[0] or a in i[1]:
                print("[{}] {} {}".format(idx+1, i[0], i[1]))
                idx += 1
        if idx == 0:
            print("조회된 자료가 없습니다.")

    elif m == "2":# 입력
        print("2. 입력")
        a = input("입력할 이름을 입력하세요: ").strip()
        b = input("입력할 전화번호를 입력하세요: ").strip()
        if a == "" or b == "":
            print("입력값이 부족합니다. 다시 입력해주세요.")
            continue

        phonebook.append([a, b])
        print("{} {} 입력 성공".format(a, b))

    elif m == "3":# 수정
        print("3. 수정")
        a = input("이름을 입력하세요: ").strip()
        b = input("변경할 전화번호를 입력하세요: ").strip()
        if a == "" or b == "":
            print("입력값이 부족합니다. 다시 입력해주세요.")
            continue

        idx = 0
        cnt = 0
        for i in phonebook:
            if i[0] == a:
                phonebook[idx][1] = b
                cnt += 1
            idx += 1

        if cnt > 0:
            print("{} {} 수정 성공".format(a, b))
        else:
            print("{} 이름이 존재하지 않습니다.".format(a))


    elif m == "4":# 삭제
        print("4. 삭제")
        a = input("삭제할 전화번호를 입력하세요: ").strip()
        if a == "":
            print("입력값이 부족합니다. 다시 입력해주세요.")
            continue

        del_cnt = 0

        for i in phonebook:
            if i[1] == a:
                phonebook.remove([i[0], i[1]])
                del_cnt += 1

        if del_cnt > 0:
            print("{} 삭제 성공".format(a))
        else:
            print("{} 번호가 존재하지 않습니다.".format(a))

        
    elif m == "5":# 종료
        break
