

n=int(input())
ds=[[100]*(n+1) for _ in range(n+1)]
while True:
    x,y=map(int,input().split())
    if x==-1 and y==-1:
        break
    else:
        ds[x][y]=1
        ds[y][x]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
                    ds[i][j]=min(ds[i][j],ds[i][k]+ds[k][j])


result=[0]*(n+1)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(ds[i][j],end=' ')
#     print()
for i in range(1, n + 1):
    m=0
    for j in range(1, n + 1):
            m= max(m,ds[i][j])
    result[i]=m
# print(result)
num=[]
minC=1000
for i in range(1,n+1):
    minC=min(minC,result[i])

for i in range(1,n+1):
    if result[i] == minC:
        num.append(i)
print(minC,len(num))
for i in num:
    print(i,end=' ')