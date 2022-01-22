import sqlite3
 
table_name = "phonebook"
conn = sqlite3.connect("phonebook.db")
cur = conn.cursor()

def create_table():
    global conn
    try:

        cur.execute("select * from sqlite_master where type='table' and tbl_name='phonebook'")
        rows = cur.fetchall()

        if rows:
            print(f"DB(테이블) {table_name}이 이미 존재합니다. ")
        else:
            conn.execute('create table phonebook(no integer primary key autoincrement, name text, hpno text)')
            conn.commit()
            print("DB(테이블) 생성 성공")
    except:
        print("DB(테이블) 생성 실패")
    
    print_menu()
    return


def print_menu():
    print()
    print("="*60)
    print("1. 조회, 2. 입력, 3. 수정, 4. 삭제, 5. 종료, 6. DB생성")
    print("="*60)


def phonebook_search():
    global conn, cur
    print("1. 조회")
    a = input("조회할 이름 또는 전화번호를 입력하세요: ").strip()
    
    cur.execute("select * from phonebook where (name like '%"+a+"%' or hpno like '%"+a+"%')")
    rows = cur.fetchall()

    idx = 0
    for row in rows:
        print("[{}] {} {}".format(row[0], row[1], row[2]))
        idx += 1
    
    if idx == 0:
        print("조회된 자료가 없습니다.")

    print_menu()
    return


def phonebook_insert():
    global conn, cur
    print("2. 입력")
    a = input("입력할 이름을 입력하세요: ").strip()
    b = input("입력할 전화번호를 입력하세요: ").strip()
    if a == "" or b == "":
        print("입력값이 부족합니다. 다시 입력해주세요.")
        phonebook_insert()
        return

    try:
        cur.execute('insert into phonebook (name, hpno) values (?, ?)', (a, b))
        conn.commit()

        print("{} {} 입력 성공".format(a, b))
    except:
        print("{} {} 입력 실패".format(a, b))
    
    print_menu()
    return

def phonebook_update():
    global conn, cur
    print("3. 수정")
    a = input("이름을 입력하세요: ").strip()
    b = input("변경할 전화번호를 입력하세요: ").strip()
    if a == "" or b == "":
        print("입력값이 부족합니다. 다시 입력해주세요.")
        phonebook_update()
        return

    try:
        cur.execute('update phonebook set hpno=? where name=?', (b, a))
        conn.commit()
        print("{} {} 수정 성공".format(a, b))
    except:
        print("{} {} 수정 실패".format(a, b))

    print_menu()
    return

def phonebook_delete():
    global conn, cur
    print("4. 삭제")
    a = input("삭제할 전화번호를 입력하세요: ").strip()
    if a == "":
        print("입력값이 부족합니다. 다시 입력해주세요.")
        phonebook_delete()
        return

    try:
        cur.execute('delete from phonebook where hpno=?', (a,))
        conn.commit()
        print("{} 삭제 성공".format(a))
    except:
        print("{} 삭제 실패".format(a))

    print_menu()
    return
 

print("파이썬 전화번호부 Ver 1.0")
print_menu()

while True:
    m = input("기능을 선택하세요.(1~6 입력) ").strip()
    if m == "": continue

    if m == "1":
        phonebook_search()

    elif m == "2":
        phonebook_insert()

    elif m == "3":
        phonebook_update()

    elif m == "4":
        phonebook_delete()
        
    elif m == "5":
        break

    elif m == "6":
        create_table()

cur.close()
conn.close()
