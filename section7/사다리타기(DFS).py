'''
사다리 타기(DFS)
현수와 친구들은 과자를 사먹기 위해 사다리 타기를 합니다. 사다리 표현은 2차원 평면은 0으
로 채워지고, 사다리는 1로 표현합니다. 현수는 특정도착지점으로 도착하기 위해서는 몇 번째
열에서 출발해야 하는지 알고싶습니다. 특정 도착지점은 2로 표기됩니다. 여러분이 도와주세
요. 사다리의 지도가 10*10이면
0 1 2 3 4 5 6 7 8 9
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1
특정목적지인 2에 도착하려면 7번 열 출발지에서 출발하면 됩니다.
▣ 입력설명
10*10의 사다리 지도가 주어집니다.
▣ 출력설명
출발지 열 번호를 출력하세요.
출발지 열번호
[자료구조와 알고리즘]
- 19 -
▣ 입력예제 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1
▣ 출력예제 1
7

'''
import sys
def DFS(x,y,start):
    if board[x][y]==2:
        print(start)
        sys.exit()
    if 1<=x<=10 and 0<=y+1<=9 and board[x][y+1]!=0 and ch[x][y+1]==0:
        ch[x][y+1]=1
        DFS(x,y+1,start)
        ch[x][y+1]=0
    elif 1<=x<=10 and 0<=y-1<=9 and board[x][y-1]!=0and ch[x][y-1]==0:
        ch[x][y-1]=1
        DFS(x,y-1,start)
        ch[x][y-1]=0
    elif 1<=x+1<=10 and 0<=y<=9 and board[x+1][y]!=0and ch[x+1][y]==0:
        ch[x+1][y]=1
        DFS(x+1,y,start)
        ch[x+1][y]=0
    else:
        return

if __name__ == '__main__':

    board=[]
    res=[]
    ch=[[0]*10 for _ in range(11)]
    for i in range(10):
        res.append(i)
    board.append(res)
    for i in range(10):
        res = list(map(int,input().split()))
        board.append(res)

    for i in range(10):
        if board[1][i]==1:
            DFS(1,i,i)

