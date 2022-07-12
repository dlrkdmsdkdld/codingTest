def DFS(L,now,total):
    global cnt
    if L ==n:
        if total>cnt:
            cnt = total
    else:
        if now<res[L]:
            DFS(L+1,res[L],total+1)
            DFS(L+1,now,total)
        else:
            DFS(L+1,now,total)


if __name__ == '__main__':
    n=int(input())
    res = list(map(int,input().split()))
    ch=[0]*(n+1)
    focus=[]
    cnt=0
    check=0
    for i in range(1,n+1):
        focus.append(i)
    DFS(0,0,0)
    print(cnt)