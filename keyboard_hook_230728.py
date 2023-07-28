import keyboard
import threading
import pyautogui
from time import sleep
import os


class Hook(threading.Thread):
    def __init__(self):
        super(Hook, self).__init__()  # 부모 클래스 __init__ 실행
        self.daemon = True  # 데몬 쓰레드로 설정
        self.event = False  # f4가 눌리면 event 발생
        self.my_xy = []     # 좌표 저장 리스트
        keyboard.unhook_all()  # 후킹 초기화
        keyboard.add_hotkey('f4', print, args=['\n종료합니다'])  # f4가 눌리면 print 실행
        keyboard.add_hotkey('f2', print, args=['\n좌표값이 추가되었습니다'])  # f2가 눌리면 print 실행
        
    def run(self):  # run 메소드 재정의  
        while True:
            key = keyboard.read_hotkey(suppress=False)  # hotkey를 계속 읽음
            if key == 'f4':  # f4 받은 경우
                self.event = True  # event 클래스 변수를 True로 설정
                # print("\n", self.my_xy)

                with open(r"config.txt", "w") as f:
                    for i in self.my_xy:
                        f.write("{},{}\n".format(i[0], i[1]))
               
                break  # 반복문 탈출
            
            elif key == 'f2':
                position = pyautogui.position()
                self.my_xy.append((position.x, position.y))


def track_pos():
    h = Hook()  # 훅 쓰레드 생성
    h.start()   # 쓰레드 실행
    print('size:', pyautogui.size())  # 화면 크기 출력
    
    while True: # 무한루프
        if h.event == True:  # h.event가 True이면(f4 입력받은 경우) 종료
            break
        position = pyautogui.position()  # 마우스 현재 위치(x, y) 반환
        print(f'\r{position.x:4}, {position.y:4}', end='')
        sleep(0.05)
    h.join()    # 쓰레드 종료까지 대기
    keyboard.unhook_all()  # 후킹 해제


try:
    cur_path = os.path.dirname(os.path.realpath(__file__))
    with open(cur_path+"/memo.txt", "r") as f:
        print(f.readline())
except:
    pass

track_pos()