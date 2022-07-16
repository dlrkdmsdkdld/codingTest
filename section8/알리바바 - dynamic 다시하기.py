
if __name__ == '__main__':
    n=int(input())
    board=[]
    result=10000
    for i in range(n):
        res=list(map(int,input().split()))
        board.append(res)
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=board[0][0]
    for i in range(n):
        dy[0][i]=dy[0][i-1]+board[0][i]
        dy[i][0]=dy[i-1][0]+board[i][0]
    for i in range(1,n):
        for j in range(1,n):
            dy[i][j]=min(dy[i-1][j],dy[i][j-1])+board[i][j]
    print(dy[n-1][n-1])