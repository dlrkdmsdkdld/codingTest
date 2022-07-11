
k,n = map(int,input().split())
res=[]
largest=0
for i in range(k):
    tmp = int(input())
    res.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
# rt=500
cnt = 0
result=0
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    for i in res:
        tmp=i//mid
        cnt+=tmp

    if cnt>= n:
        result=mid
        lt=mid+1
    else:
        rt=mid-1
print(result)