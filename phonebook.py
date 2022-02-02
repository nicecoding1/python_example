import pickle
import os.path

def print_menu():
    print()
    print("="*50)
    print("1. 조회, 2. 입력, 3. 수정, 4. 삭제, 5. 종료")
    print("="*50)

def phonebook_search():
    global phonebook
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

    print_menu()
    return

def phonebook_insert():
    global phonebook
    print("2. 입력")
    a = input("입력할 이름을 입력하세요: ").strip()
    b = input("입력할 전화번호를 입력하세요: ").strip()
    if a == "" or b == "":
        print("입력값이 부족합니다. 다시 입력해주세요.")
        phonebook_insert()
        return

    phonebook.append([a, b])
    print("{} {} 입력 성공".format(a, b))
    print_menu()
    return

def phonebook_update():
    global phonebook
    print("3. 수정")
    a = input("이름을 입력하세요: ").strip()
    b = input("변경할 전화번호를 입력하세요: ").strip()
    if a == "" or b == "":
        print("입력값이 부족합니다. 다시 입력해주세요.")
        phonebook_update()
        return

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

    print_menu()
    return

def phonebook_delete():
    global phonebook
    print("4. 삭제")
    a = input("삭제할 전화번호를 입력하세요: ").strip()
    if a == "":
        print("입력값이 부족합니다. 다시 입력해주세요.")
        phonebook_delete()
        return

    tmp_list = []

    find = 0
    for i in phonebook:
        if not i[1] == a:
            tmp_list.append([i[0], i[1]])
        else:
            find += 1

    phonebook.clear()
    phonebook = tmp_list

    if find > 0:
        print("{} 삭제 성공".format(a))
    else:
        print("{} 번호가 존재하지 않습니다.".format(a))

    print_menu()
    return

def save_phonebook():
    global phonebook
    with open("phonebook.pickle", "wb") as f:
        pickle.dump(phonebook, f, pickle.HIGHEST_PROTOCOL)

"""
[
['홍길동','010-1234-5678'],
['김철수','010-1234-5555'],
['김대한','010-1111-2222']    
]
"""

phonebook = []

if os.path.exists("phonebook.pickle"):
    with open("phonebook.pickle", "rb") as f:
        phonebook = pickle.load(f)

print("파이썬 전화번호부 Ver 1.0")
print_menu()

while True:
    m = input("기능을 선택하세요.(1~5 입력) ").strip()
    if m == "": continue

    if m == "1":
        phonebook_search()

    elif m == "2":
        phonebook_insert()
        save_phonebook()

    elif m == "3":
        phonebook_update()
        save_phonebook()

    elif m == "4":
        phonebook_delete()
        save_phonebook()
        
    elif m == "5":
        save_phonebook()
        break
