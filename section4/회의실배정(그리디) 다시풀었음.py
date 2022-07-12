
n=int(input())
res=[]
for i in range(n):
    x,y= map(int,input().split())
    res.append((x,y))
res=sorted(res,key=lambda x : x[1])
# print(res)
end=0
cnt=0
for i in res:
    if end <= i[0]:
        end = i[1]
        cnt+=1
print(cnt)