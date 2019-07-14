bc=list(input())
tt=len(bc)
new=''
for l in range (0,tt,2):
    bc[i],bc[i+1]=bc[i+1],bc[i]
print(*bc,sep='')
