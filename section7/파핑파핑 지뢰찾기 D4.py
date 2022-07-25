import sys
'''
파핑 파핑 지뢰 찾기’라는 유명한 게임이 있다. 이 게임은 RXC 크기의 표를 이용하는 게임인데,

표의 각 칸에는 지뢰가 있을 수도 있고 없을 수도 있다.

표의 각 칸을 클릭했을 때, 그 칸이 지뢰가 있는 칸이라면 ‘파핑 파핑!’이라는 소리와 함께 게임은 끝난다.

지뢰가 없는 칸이라면 변이 맞닿아 있거나 꼭지점이 맞닿아 있는 최대 8칸에 대해 몇 개의 지뢰가 있는지가 0에서 8사이의 숫자로 클릭한 칸에 표시된다.

만약 이 숫자가 0이라면 근처의 8방향에 지뢰가 없다는 것이 확정된 것이기 때문에 그 8방향의 칸도 자동으로 숫자를 표시해 준다.

실제 게임에서는 어떤 위치에 지뢰가 있는지 알 수 없지만, 이 문제에서는 특별히 알 수 있다고 하자.

지뢰를 ‘*’로, 지뢰가 없는 칸을 ‘.’로, 클릭한 지뢰가 없는 칸을 ‘c’로 나타냈을 때 표가 어떻게 변화되는지 나타낸다.
 



세 번째 예에서는 0으로 표시 될 칸들과 이와 인접한 칸들이 한 번의 클릭에 연쇄적으로 숫자가 표시된 것을 볼 수 있다.

파핑 파핑 지뢰 찾기를 할 때 표의 크기와 표가 주어질 때, 지뢰가 있는 칸을 제외한 다른 모든 칸의 숫자들이 표시되려면 최소 몇 번의 클릭을 해야 하는지 구하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에 하나의 정수 N(1 ≤ N ≤ 300) 이 주어진다. 이는 지뢰 찾기를 하는 표의 크기가 N*N임을 나타낸다.

다음 N개의 줄의 i번째 줄에는 길이가 N인 문자열이 주어진다.

이 중 j번째 문자는 표에서 i번째 행 j번째 열에 있는 칸이 지뢰가 있는 칸인지 아닌지를 나타낸다.

‘*’이면 지뢰가 있다는 뜻이고, ‘.’이면 지뢰가 없다는 뜻이다. ‘*’와 ‘.’외의 다른 문자는 입력으로 주어지지 않는다.
입력
2
3
..*
..*
**.
5
..*..
..*..
.*..*
.*...
.*...
 

[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

최소 몇 번의 클릭을 해야 지뢰가 없는 모든 칸에 숫자가 표시될 것인지 출력한다.
#1 2
#2 8
'''
def printZero(x,y,c):
    global data
    global ClickNum
    Fcnt=0
    # for z in data:
    #     print(z)
    # print("-----------")
    if data[x][y] != '.':
        return
    if c==0:
        for d in Direction:
            xx = d[0] + x
            yy = d[1] + y
            if 0 <= xx < n and 0 <= yy < n:
                if data[xx][yy] == '*':
                    Fcnt += 1
    else:
        Fcnt=0
    if Fcnt==0 and c==0:
        ClickNum+=1

    if Fcnt==0:
        data[x][y]=0
        for d in Direction:
            xx = d[0] + x
            yy = d[1] + y
            if 0 <= xx < n and 0 <= yy < n:
                spreadPrint(xx,yy)
    else:
        return

def spreadPrint(x,y):
    global nextTarget
    Fcnt=0
    for d in Direction:
        xx = d[0] + x
        yy = d[1] + y
        if 0 <= xx < n and 0 <= yy < n:
            if data[xx][yy] == '*':
                Fcnt += 1
    if Fcnt==0:
        printZero(x,y,1)
    data[x][y]=Fcnt
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
Direction = [ (1,0),(0,1) , (-1,0),(0,-1) , (1,1),(1,-1),(-1,1),(-1,-1)   ]
T = 1
for test_case in range(1, T + 1):
    ClickNum=0
    n = int(input())
    data = []
    for i in range(n):
        tmp  = list(input())
        data.append(tmp)
    # for i in data:
    #     print(i)
    cnt=0
    check =0
    nextTarget=[]
   # while '.' not in data:
    for w in range(n):
        for j in range(n):
            if data[w][j]=='.':
                printZero(w,j,0)
    for w in range(n):
        for j in range(n):
            if data[w][j]=='.':
                ClickNum+=1
    print(ClickNum)

        # data[save[0]][save[1]] = Fcnt
        # printZero(save[0],save[1])


