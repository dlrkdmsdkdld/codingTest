
# 1. 나무를 최대한 떨어뜨렸을 때, 그 때의 거리를 구한다.
# 2. 그 거리를 만들기 위해 심어야 하는 나무의 최소 갯수를 구한다.

n = int(input())
valList = [0 for _ in range(100005)]
testList = list()

def getGCD(a, b):
  while b:
      a,b=b,a%b
  return a

for i in range(n):
  valList[i] = int(input())

GCD = 0
for i in range(n-1):
  distance = valList[i+1] - valList[i]
  if i == 0:
    GCD = distance
  else:
    GCD = getGCD(GCD, distance)

#***
# 2 18 26 30
# 2 6 10 14 18 22 26 30 ----> 30-2 = 28 / 4 --> 7(간격) --> 나무는 8그루
# GCD : 4
totalTreeCnt = int((valList[n-1] - valList[0]) / GCD) + 1


print(totalTreeCnt-n)
### 내 답 #######################
## template
n=int(input())
res = []
tmp=0
last=0
di=[]
for i in range(n):
  tmp=int(input())
  di.append(tmp - last)
  res.append(tmp)
  last=tmp
di.pop(0)
# print(di)
minnum = min(di)
for i in range(minnum,0,-1):
  for z in di:
    if z%i==0:
      ok=1
    else:
      ok=0
      break
  if ok==1:
    minnum=i
    break

totalcnt = ((res[n-1] - res[0])//minnum )+1 #가장 먼거리에서 가장 가까운거리빼서 간격마다 심었을때의 수
# 이미 n개가 심어있으므로 n개 뺌
print(totalcnt-n)


