pl=int(input())
e=0
rv=0
while pl>0 :
 e=pl%10
 rv=rv*10+e
 pl=pl//10
print(rv) 
