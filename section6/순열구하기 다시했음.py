def DFS(L,da):
    global cnt
    if L==m:
        cnt+=1
        for i in da:
            print(i,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                da.append(i)
                DFS(L+1,da)
                da.pop()
                ch[i]=0


if __name__ == '__main__':
    n,m = map(int,input().split())
    cnt=0
    data=[]
    ch=[0]*(n+1)
    DFS(0,data)
    print(cnt)