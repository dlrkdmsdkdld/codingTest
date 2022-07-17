def DFS(L,sum):
    global res
    if L ==k:
        result.add(abs(sum))
    else:
        DFS(L+1,sum+res[L])
        DFS(L+1,sum-res[L])
        DFS(L+1,sum)
if __name__ == '__main__':
    k= int(input())
    res= list(map(int,input().split()))
    m=sum(res)
    result=set()
    ch=[0]*(m+1)

    DFS(0,0)
    result=list(result)
    result.sort()
    cnt=0
    for i in result:
        ch[i]+=1
    for i in range(1,m+1):
        if ch[i]==0:
            cnt+=1

    print(cnt)
