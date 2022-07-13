n=int(input())
data=[]
for i in range(n):
    a,b,c=map(int,input().split())
    data.append((a,b,c))
data.sort(reverse=True)
dy=[0]*(n)
dy[0]=data[0][1]
for i in range(1,n):
    m=0
    check=True
    for j in range(i-1,-1,-1):
        if data[j][2]>data[i][2] and m < data[i][1]+dy[j]:
            m=data[i][1]+dy[j]
            check=False
    if check:
        dy[i]=data[i][1]
    else:
        dy[i]=m
tmp = max(dy)
print(tmp)