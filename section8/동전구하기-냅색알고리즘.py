

if __name__ == '__main__':
    n=int(input())
    res=list(map(int,input().split()))
    m=int(input())
    dy=[1000]*(m+1)
    dx=[0]*(m+1)
    for i in res:
        dy[i]=1
        for j in range(i,m+1):
            dy[j]=min(dy[j-i]+1,dy[j])
            # dy[j]=min(dy[j],tmp)

    print(dy[m])
