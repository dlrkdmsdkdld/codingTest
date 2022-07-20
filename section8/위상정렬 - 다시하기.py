

n,m = map(int,input().split())
des = [0]*(n+1)
dy=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    des[y]+=1
    dy[x][y]=1
q=[]
result=[]
for i in range(1,n+1):
    if des[i]==0:
        q.append(i)

while q:
    tmp = q.pop(0)
    result.append(tmp)
    for j in range(1,n+1):
        if dy[tmp][j]==1 :
            des[j]-=1
            if des[j]==0:
                q.append(j)

for i in result:
    print(i,end=' ')


