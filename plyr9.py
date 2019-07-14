ni= []
def drime(o):
    z = 0
    for x in range(2,o-1):
        if o%x == 0:
            z =1
            break
    if not z:
        ni.append(o)

a ,yt = map(int,input().split())

for e in range(a,yt+1):
    drime(e)
print(len(ni))
