import sys
def DFS(L,data):
    if L==n:
        x=0

        for i in range(0,n):
           x+=result[i]*data[i]
        # print(data,x)
        if x==m:
            for i in data:
                print(i,end=' ')
            sys.exit()
    else:
        for a in range(1,n+1):
            if ch[a] == 0:
                ch[a]=1
                data.append(a)
                DFS(L+1,data)
                data.pop()
                ch[a]=0


if __name__ == '__main__':
    n ,m=map(int,input().split())

    cnt=0
    res=[0]*m
    ch=[0]*(n+1)
    d=[]
    result=[]
    n = n - 1
    for i in range(0, n+1):
        r=i
        tmp =1
        rtmp=1
        for j in range(1,n+1):
            tmp*=j
        for j in range(1,r+1):
            rtmp*=j
        tmp=tmp//rtmp
        rtmp=1
        k=n-r
        for j in range(1,k+1):
            rtmp*=j
        tmp=tmp//rtmp
        result.append(tmp)
    # print(result)
    n+=1
    DFS(0,d)