def Count(x):
    cnt=0
    tmp=0
    for i in res:
        if tmp+i>x:
            cnt+=1
            tmp=i
        else:
            tmp+=i
    if tmp !=0:
        cnt +=1
    return cnt
n,m = map(int,input().split())
res = list(map(int,input().split()))
lt=max(res)
rt = 10000
result=10000
while lt<=rt:
    mid = (lt+rt)//2
    tmp = Count(mid)
    if tmp >m:
        lt = mid+1
    else:
        if tmp == m:
            result=min(result,mid)
        rt = mid - 1
print(result)

