# 제너레이터에 사용할 함수
def count_seq():
   # 초기값
   n='2'
   while True:
       # 첫번째 함수 호출 시 int(n)을 리턴
       yield int(n)
       next_value=''

       # 두번째 호출부터 아래 코드 실행
       while len(n)>0:
           # 값의 처음값을 first에 저장, count 0으로 초기화
           first=n[0]
           count=0  

           # 같은 값이 반복되면 카운트 증가
           # 값을 다음 자릿수로 이동(리스트 슬라이싱)
           while len(n)>0 and n[0]==first:
               count+=1
               n=n[1:]

           # 변환된 값을 연결(문자열에서 + 은 문자열 연결)
           next_value+='{}{}'.format(count,first)

       n=next_value


if __name__ == '__main__':
   # 제너레이터 사용을 위해 함수 변수 선언
   gen=count_seq()

   # 10번 반복
   for i in range(10):
       # 제너레이터 호출은 next()으로 한다
       print(next(gen))
        
"""
[실행 결과]
2
12
1112
3112
132112
1113122112
311311222112
13211321322112
1113122113121113222112
31131122211311123113322112
"""
