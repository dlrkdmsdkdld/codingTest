'''
단지 번호 붙이기(DFS, BFS)
그림1과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸
다.철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한
다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
그림2는 그림1을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지
에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0

0 1 1 0 2 0 0
0 1 1 0 2 0 2
1 1 1 0 2 0 2
0 0 0 0 2 2 2
0 3 0 0 0 0 0
0 3 3 3 3 3 0
0 3 3 3 0 0 0
 [그림 1] [그림 2]
▣ 입력설명
첫 번째줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력
되고 그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다
▣ 출력설명
첫 번째줄에는 총 단지수를 출력하시오. 그리고 각 단지내의 집의 수를 오름차순으로 정렬하
여 한줄에 하나씩 출력하시오
▣ 입력예제 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
▣ 출력예제 1
3
7
8
9


'''
from collections import deque
point=[(1,0),(0,1),(-1,0),(0,-1)]
def DFS(x,y):
    global num
    for i in point:
        if 0<=x+i[0]<=n-1 and 0<=y+i[1]<=n-1 and board[x+i[0]][y+i[1]]==1 and ch[x+i[0]][y+i[1]]==0:
            ch[x + i[0]][y + i[1]]=1
            num+=1
            DFS(x+i[0],y+i[1])
if __name__ == '__main__':
    n=int(input())
    board=[]
    num=0
    ch=[[0]*n for _ in range(n)]
    Lx,Ly=0,0
    for i in range(n):
        tmp=input()
        res=[]
        for k in tmp:
            res.append(int(k))
        board.append(res)

    cnt=0
    result=[]
    Q=deque()
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                Q.append((i,j))
    while Q:
        tmp=Q.popleft()
        num=0
        DFS(tmp[0],tmp[1])
        if num!=0:
            cnt+=1
            result.append(num)
    result.sort()
    print(cnt)
    for i in result:
        print(i)
