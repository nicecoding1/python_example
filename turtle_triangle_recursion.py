from turtle import *
import math

step = int(input("삼각형 그리기 재귀함수 반복 횟수 입력: "))
size = 400
if step < 1:
    min = size
elif step == 1:
    min = size / 2
else:
    min = size / (2**step)

#pf = 0.8660254  # 피타고라스정리: sqrt(3)/2
pf = math.sqrt(3)/2

# r,g,b 색상 만들어 반환하는 함수
def getRGB():
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def D(l, x, y):
    if l > min:  # 변의 길이가 최소 길이보다 길면 재귀함수 호출(변 사이즈 반으로 줄여서 호출)
        l = l / 2  # 크기를 반으로 줄이고 실행
        D(l, x, y)  # 왼쪽 아래 삼각형
        D(l, x + l, y)  # 오른쪽 아래 삼각형
        D(l, x + l / 2, y + l * pf)  # 위쪽 삼각형
    else:  # 재귀함수 종료
        goto(x, y);

        r, g, b = getRGB()
        color(r, g, b)

        pendown()  # 선그리기 시작
        forward(l); # l만큼 직진
        left(120)  # 120도 좌회선
        forward(l); # l만큼 직진
        left(120)  # 120도 좌회전
        forward(l)  # l만큼 직진
        setheading(0)  # 거북이 방향 초기화
        penup(); # 선그리기 종료
        goto(x, y) # 시작 지점으로 이동


penup()
speed('fastest') #빠르게 그림 그리기
D(size, -size / 2, -size * pf / 2.0)
goto(0, 0)
done()
