import heapq as hq
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            tmp =hq.heappop(a)
            print(tmp[1])
    else:
        hq.heappush(a,(-n,n)) #우선순위를 마이너스로 주어서 가장 큰값이 맨위로가게 조작











