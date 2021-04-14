import time, os
from datetime import datetime

def save_log(msg):
    if msg == "":
        return
    
    now_dt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    file_dt = datetime.today().strftime("%Y%m%d")

    with open("python_cron_"+file_dt+".txt", "a") as f:
        f.write("["+now_dt+"] "+msg+"\n")

while True:
    now = time.localtime()
    now_list = list(now)
    hr = now_list[3]
    min = now_list[4]
    day = now_list[6] #monday: 0, sunday: 6

    # 1min
    os.system("/usr/bin/php /home/cron/test.php")
    save_log("test.php")

    # 2min
    if min % 2 == 0:
        os.system("")
        save_log("")

    # 5min
    if min % 5 == 0:
        os.system("")
        save_log("")

    # everyday 4:00 am
    if hr == 4 and min == 0:
        os.system("")
        save_log("")

    # sunday 5:10 am
    if day == 6 and hr == 5 and min == 10:
        os.system("")
        save_log("")

    time.sleep(60)