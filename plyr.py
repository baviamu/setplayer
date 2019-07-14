bc=list(input())
tt=len(bc)
new=''
for l in range (0,tt,2):
    bc[l],bc[l+1]=bc[l+1],bc[l]
print(*bc,sep='')
