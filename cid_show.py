import datetime
import time
import serial
import pymysql

region_code = {
    "010":"핸드폰",
	"02":"서울", "031":"경기", "032":"인천", "033":"강원",
	"041":"충남", "042":"대전", "043":"충북",
	"051":"부산", "052":"울산", "053":"대구", "054":"경북", "055":"경남",
	"061":"전남", "062":"광주", "063":"전북", "064":"제주"
}

conn = pymysql.connect(host="localhost", user="root", password="", db="test")

ser = serial.Serial('COM9', 19200, timeout=1)

while True:
    s = ser.read(100)
    cid = s.decode('utf-8')
    tel = cid[1:-1]
    dt = datetime.datetime.now()
    print("\r"+dt.strftime("%Y-%m-%d %H:%M:%S"), end="")

    if len(tel) >= 4:
        try:
            curs = conn.cursor()
            sql = "select * from phonebook where telno=%s"
            curs.execute(sql, (tel,))
            rows = curs.fetchall()
            name = memo = ""
            for row in rows:
                name = row[2]
                memo = row[3]

            region = ""
            if tel[0:2] in region_code:
                region = region_code[tel[0:2]] + " "
            elif tel[0:3] in region_code:
                region = region_code[tel[0:3]] + " "

            f = open("cid_info.txt", "a", encoding="utf-8")
            dt = datetime.datetime.now()
            print("\n"+dt.strftime("%Y-%m-%d %H:%M:%S") + " --> " + tel + " " + region+ " " + name+ " " + memo)
            f.write(dt.strftime("%Y-%m-%d %H:%M:%S") + " --> " + tel + " " + region+ " " + name+ " " + memo + "\n")
            f.close()
        except Exception as e:
            print(e)

    time.sleep(0.3)
