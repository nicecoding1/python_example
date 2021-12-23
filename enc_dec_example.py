import os.path
import string
import random
import pickle

def print_menu():
    print()
    print("암호화/복호화 프로그램입니다 ^o^")
    print("1. 암호화")
    print("2. 복호화")
    print("3. 종료")
    print()

def record_file_in_check(f):
    record = []
    if not os.path.isfile("record.txt"):
        with open("record.txt", "w", encoding="utf8"):
            pass
        return False
    with open("record.txt", "r", encoding="utf8") as file:
        record = file.read()
        if record.find(f) == -1:
            return False
        else:
            return True

while True:
    print_menu()
    m = input("원하시는 기능을 선택하세요: ")

    if m == "1":
        f = input("암호화를 할 파일 이름을 입력하세요: ")
        if not os.path.isfile(f):
            print("파일이 존재하지 않습니다.")
            continue

        test = record_file_in_check(f)
        if test: 
            print("이미 암호화가 완료된 파일입니다.")
            continue

        enc_key = string.ascii_letters + string.digits
        t = list(enc_key)
        random.shuffle(t)
        enc_value = "".join(t)

        keylist = {}
        for i in range(len(enc_key)):
            keylist[enc_key[i]] = enc_value[i]

        f2 = f[:f.index('.')]+".pwd"
        with open(f2, "wb") as _f:
            pickle.dump(keylist, _f, pickle.HIGHEST_PROTOCOL)

        src_data = ""
        with open(f, "r", encoding="utf8") as _f:
            src_data = _f.read()

        enc_data = ""
        for i in src_data:
            if i in keylist:
                enc_data += keylist[i]
            else:
                enc_data += i

        with open(f, "w", encoding="utf8") as _f:
            _f.write(enc_data)

        with open("record.txt", "a", encoding="utf8") as _f:
            _f.write(f+"\n")

        print("암호화를 완료했습니다.")

    elif m == "2":
        f = input("복호화를 할 파일 이름을 입력하세요: ")
        if not os.path.isfile(f):
            print("파일이 존재하지 않습니다.")
            continue

        test = record_file_in_check(f)
        if not test: 
            print("암호화 되지 않은 파일입니다.")
            continue
        
        f2 = f[:f.index('.')]+".pwd"

        keylist = {}
        keyreverse = {}
        with open(f2, "rb") as _f:
            keylist = pickle.load(_f)

        for i in keylist:
            _v = keylist[i]
            keyreverse[_v] = i

        enc_data = ""
        with open(f, "r", encoding="utf8") as _f:
            enc_data = _f.read()

        src_data = ""
        for i in enc_data:
            if i in keyreverse:
                src_data += keyreverse[i]
            else:
                src_data += i

        with open(f, "w", encoding="utf8") as _f:
            _f.write(src_data)
        
        print("복호화를 완료했습니다.")

    elif m == "3":
        break

    else:
        print("잘못된 입력입니다.")
        continue