'''
1 부터 나선 형 모양으로 배열에 값을 넣은 후 출력하는 프로그램을 작성하시오.

입력은 배열의 크기 n 이 주어진다. n * n 행 배열이다. ( 3 <= n <= 25)
ex 3
출력
각 숫자 사이 한 칸의 공백을 가지고 나선형(달팽이) 배열을 출력한다.
1 2 3
8 9 4
7 6 5
'''
def DFS(x,y,diN,data):
    if res[x][y]==0:
        res[x][y]=data
        pos=di[diN]
        xx=x+pos[0]
        yy=y+pos[1]
        if 0<=xx<=n-1 and 0<=yy<=n-1 and res[xx][yy] ==0:
            DFS(xx,yy,diN,data+1)
        else:
            if diN+1==4:
                diN=-1
            xx=x+di[diN+1][0]
            yy=y+di[diN+1][1]
            if 0<=xx<=n-1 and 0<=yy<=n-1:
                DFS(xx,yy,diN+1,data+1)


di = [(0,1),(1,0),(0,-1),(-1,0)  ]
if __name__ == '__main__':
    n = int(input())
    res = [[0] * (n) for _ in range(n)]
    DFS(0,0,0,1)
    for i in res:
        for j in i:
            print(j,end=' ')
        print()



