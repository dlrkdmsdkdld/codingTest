## template
import math
def Prim(x):
    a = 0
    for z in range(2, int(math.sqrt(x) + 1)):
        if x % z == 0:
            a = 1
            break
    if a == 0:
        return 1
    else:
        return 0


res = []
while True:
    tmp = int(input())
    if tmp == 0:
        break
    res.append(tmp)

a = [False, False] + [True] * (max(res) * 2)
primes = []

for i in range(2, (max(res) * 2) + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, (max(res) * 2) + 1, i):
            a[j] = False
while res:
    tmp = res.pop(0)
    cnt=0
    for i in primes:
        if tmp+1<=i<=tmp*2:
            cnt+=1
        elif i>tmp*2:
            break

    print(cnt)

