## template
'''
입력
첫 줄에는 격자 크기를 나타내는 정수 C와 R이 하나의 공백을 사이에 두고 차례대로 주어진다. 두 값의 범위는 5 ≤ C, R ≤ 20이다. 그다음 줄 부터 총 R줄에 걸쳐 맵의 상태를 나타내는 숫자들이 공백을 사이에 두고 주어진다. 0은 아직 채워지지 않은 칸을 나타내며 1은 채워져있는 칸을 나타낸다.

출력
작대기를 왼쪽에서 X번째 자리에 두었을 때 가장 높은 점수를 얻을 수 있고 그 때 완전히 메워지는 수평선의 개수가 Y개라면, Y를 최대로 만드는 X와 그 때의 Y를 하나의 공백을 사이에 두고 출력해야 한다.

만약 어떤 자리에 두어도 수평선을 하나도 메울 수 없거나 게임오버가 일어나는 경우라면 X와 Y를 둘다 0으로 출력한다.(게임오버는 새로 내려온 작대기가 맵상을 벗어난 경우에 일어난다. 새로나온 작대기가 맵의 가장자리에 걸쳐있는 경우는 게임오버가 아니다.)

예제 입력
6 7
0 0 0 0 0 0
0 0 0 0 0 0
1 1 1 0 0 1
1 1 1 0 0 1
1 1 1 0 1 1
1 1 1 0 1 1
1 1 1 0 1 1
예제 출력
4 3
'''
import copy
import sys
def check(x, tmp):
    global maxcnt
    global xxx
    cnt = 0
    for i in range(r):
        ch = 1
        for j in range(c):
            if tmp[i][j] == 0:
                ch = 0
                break
        if ch == 1:
            cnt += 1
    if maxcnt < cnt:
        xxx = x
        maxcnt = cnt

if __name__ == '__main__':

  dx = (1, 0)
  c, r = map(int, input().split())
  res = []
  maxcnt = 0
  xxx = 0
  for i in range(r):
      tmp = list(map(int, input().split()))
      res.append(tmp)

  for i in range(c):  # 왼쪽부터 한줄 씩 검사
      but=0
      loc = (r , i)
      for j in range(r):
          if res[j][i] == 1:
              loc = (j, i)
              break
      tmp = copy.deepcopy(res)
      xx = loc[0]
      for step in range(4):
          xx -= dx[0]
          # print(xx)
          if 0 <= xx:
              tmp[xx][i] = 1
          else:
              but=1
              break
      if but==0:
      # sys.exit()
        check(i, tmp)
  if maxcnt==0:
    print("0 0")
  else:
    print("{} {}".format(xxx + 1, maxcnt))
