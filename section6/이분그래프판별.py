## template
import sys
def DFS(d):
  global x
  global y
  for i in ver[d]:
    if i not in x and i not in y:
      if d in x:
        y.add(i)
      else:
        x.add(i)
      DFS(i)
    else:
      if d in x and i in x:
        print("No")
        sys.exit()
      if d in y and i in y:
        print("No")
        sys.exit()


if __name__ =='__main__':
  n,m=map(int,input().split())
  x=set()
  y=set()
  ver = [[] for _ in range(n+1)]
  for i in range(m):
    a,b =map(int,input().split())
    ver[a].append(b)
    ver[b].append(a)
  x.add(1)
  DFS(1)
  print("Yes")
  # print(x)
  # print(y)
  # for i in ver:
  #   print(i)

