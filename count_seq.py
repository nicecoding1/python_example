def count_seq():
   n='2'
   while True:
       yield int(n)
       next_value=''

       while len(n)>0:
           first=n[0]
           count=0  

           while len(n)>0 and n[0]==first:
               count+=1
               n=n[1:]

           next_value+='{}{}'.format(count,first)

       n=next_value

if __name__ == '__main__':
   gen=count_seq()

   for i in range(10):
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
