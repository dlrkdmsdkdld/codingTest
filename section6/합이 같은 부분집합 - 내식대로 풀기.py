import sys
def DFS(L,sum):
    if L ==n:
        return
    if sum == k - sum:
        print("YES")
        sys.exit()
    else:
        DFS(L+1,sum+res[L])
        DFS(L+1,sum)



if __name__ == '__main__':
    n=int(input())
    res = list(map(int,input().split()))
    k=sum(res)
    ch = [0]*n

    ch=[0]*(n+1)
    DFS(0,0)
    print("NO")






