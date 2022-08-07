## template
'''
입력
8줄에 걸쳐 8x8 체스판의 상태가 주어진다. 이때 0은 기물이 없는 상태이고, 1은 알랩이의 킹을 의미하고, 2는 상대의 룩을 의미하며 3은 그 외 다른 기물들을 의미한다. (킹은 하나만 존재하며, 상대의 룩은 최대 2개까지 있을 수 있다. 그 외 기물들은 최대 29개까지 있을 수 있다.)
출력
킹이 룩에게 잡힐 가능성이 있으면 1, 아니면 0을 출력한다.
예제 입력 1
0 3 0 0 0 0 0 0
3 1 0 0 0 0 2 0
0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 1
1
'''
import sys

res = []
dx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
lookchc = 0
kingchc = 0


def move(x, y, direction):
    # for i in res:
    #     print(i)
    # print('---')
    if res[x][y] == 1:
        print(1)
        sys.exit()
    if res[x][y] == 3:
        return
    else:
        res[x][y] = 2
        xx, yy = x + dx[direction][0], y + dx[direction][1]
        if 0 <= xx <= 7 and 0 <= yy <= 7:
            move(xx, yy, direction)


for i in range(8):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        lookchc = i
    if 1 in tmp:
        kingchc = i
    res.append(tmp)
lookchc=[]
for i in range(8):
    for j in range(8):
      if res[i][j]==2:
        lookchc.append((i,j))

for i in range(8):
    if res[kingchc][i] == 1:
        kingchc = (kingchc, i)
        break
while lookchc:
  tmp=lookchc.pop(0)
  if kingchc[0] != tmp[0] and kingchc[1] != tmp[1]:
      continue
  else:
      if kingchc[0] == tmp[0]:
          for i in range(2, 4):
              move(tmp[0], tmp[1], i)
      else:
        for i in range(0,2):
          move(tmp[0],tmp[1],i)
print(0)







