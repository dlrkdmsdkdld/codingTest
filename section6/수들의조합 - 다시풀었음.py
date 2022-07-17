def DFS(L,data,z):
    global cnt
    if L==k:
        if sum(data)%m == 0:
            # print(data)
            cnt+=1
    else:
        for i in range(z,n):
            if ch[i]==0:
                ch[i]=1
                data.append(a[i])
                DFS(L+1,data,i)
                ch[i]=0
                data.pop()

if __name__ == '__main__':
    cnt=0
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=int(input())
    ch=[0]*(n)
    d=[]
    DFS(0,d,0)
    print(cnt)