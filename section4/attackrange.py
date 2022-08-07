## template
'''
입력
입력 첫째 줄에는 디펜스 게임의 맵 크기 N이 주어딘다. 맵은 N×N 크기의 2차원 형태이다. (N은 6이상 100이하의 짝수)
둘째 줄에는 유닛이 설치될 위치 X, Y와 유닛의 사거리 R이 주어진다. X는 행의 번호, Y는 열의 번호를 의미한다. (X, Y는 1이상 N이하의 자연수, R은 N/2이하의 자연수)
출력
예제 출력과 같이 유닛의 사거리를 나타내어 출력한다. (유닛의 사거리가 아무리 길어도 맵을 벗어날 수는 없다.)
예제 입력
8
4 5 3
예제 출력
0 0 0 0 3 0 0 0
0 0 0 3 2 3 0 0
0 0 3 2 1 2 3 0
0 3 2 1 x 1 2 3
0 0 3 2 1 2 3 0
0 0 0 3 2 3 0 0
0 0 0 0 3 0 0 0
0 0 0 0 0 0 0 0
예제 입력
6
2 3 3
예제 출력
3 2 1 2 3 0
2 1 x 1 2 3
3 2 1 2 3 0
0 3 2 3 0 0
0 0 3 0 0 0
0 0 0 0 0 0

'''
n = int(input())
res = [[0] * (n) for _ in range(n)]
x, y, z = map(int, input().split())
res[x - 1][y - 1] = 'x'
dx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
step = []
nextstep = []
step.append((x - 1, y - 1))
for st in range(1, z + 1):
    nextstep = []
    while step:
        tmp = step.pop(0)
        for pos in dx:
            xx = tmp[0] + pos[0]
            yy = tmp[1] + pos[1]
            if 0 <= xx <= n - 1 and 0 <= yy <= n - 1 and res[xx][yy] == 0:
                res[xx][yy] = st
                nextstep.append((xx, yy))
    step = nextstep
for i in res:
    for j in i:
        print(j, end=' ')
    print()

