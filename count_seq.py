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
