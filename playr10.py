bav,re=map(str,input().split())
bav=list(bav)
re=list(re)
count=0
for f in range(0,len(bav)):
        if(bav[f]!=re[f]):
            cnt=cnt+1
if(cnt==1):
    print("yes")
else:
    print("no")
