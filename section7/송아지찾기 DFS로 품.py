'''
송아지 찾기(BFS : 상태트리탐색)
현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 현수의 위치와 송아
지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과
같은 방법으로 이동한다.
현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수
있다. 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성
하세요.
▣ 입력설명
첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000
까지이다.
▣ 출력설명
점프의 최소횟수를 구한다.
▣ 입력예제 1
5 14
▣ 출력예제 1
3

'''

import sys
sys.setrecursionlimit(10**6)
def DFS(x,n):
    global cnt
    global e
    if n>cnt :
        return
    if x == e:
        if cnt >n:
            cnt = n

    else:
        if abs(e-x)>abs(e-x-5):
            DFS(x + 5, n + 1)
        elif abs(e-x) >abs(e-x-1):
             DFS(x+1,n+1)
        else:
            DFS(x-1,n+1)





if __name__ == '__main__':
    s,e = map(int,input().split())
    cnt =1000000000
    DFS(s,0)
    print(cnt)
