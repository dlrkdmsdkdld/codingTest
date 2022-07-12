
n=int(input())
res= list(map(int,input().split()))
data=[0]*n
for i in range(n):
    tmp = res[i]
    for j in range(0,n):
        if tmp==0 and data[j]==0:
            data[j]=i+1
            break
        if (data[j]==0 or data[j] >i) and tmp!=0:
            tmp-=1
for i in data:
    print(i,end=' ')



