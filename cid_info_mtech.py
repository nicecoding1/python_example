#install command
#python -m pip install pyserial

# -*- coding: utf-8 -*-
import requests, json, time, serial, datetime

ser = serial.Serial('COM3', 19200, timeout=1)

while True:
	s = ser.read(100)
	cid = s.decode('utf-8')
	tel = cid[1:-1]
	dt = datetime.datetime.now()

    if(len(tel) >= 4):
		try:
			f = open("cid_info.txt", "a")
			dt = datetime.datetime.now()
			print(dt.strftime("%Y-%m-%d %H:%M:%S") + " : "+tel)
			f.write(dt.strftime("%Y-%m-%d %H:%M:%S") + " : "+tel+"\n")
			url = 'https://192.168.0.10/cid_info_mtech.php?hp='+tel
			r = requests.get(url, timeout=3)
			a = r.text
			info = json.loads(a)
			print(tel+ ' --> '+str(info[0])+' '+str(info[1])+' '+str(info[2])+' '+str(info[3])+' '+str(info[4])+'\n')
			f.write(tel+ ' --> '+str(info[0])+' '+str(info[1])+' '+str(info[2])+' '+str(info[3])+' '+str(info[4])+'\n\n')
			f.close()
		except:
			pass
			f.close()
	time.sleep(1)
