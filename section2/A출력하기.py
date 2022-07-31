'''
n층의 A를 출력하는 프로그램을 작성하여라. Input, Output의 예제를 참고한다. (단, n은 항상 홀수만 주어진다.)
입력
 첫째 줄에 자연수이며, 홀수인 n이 주어진다. (5≤n≤100)
 5
 출력 예제
    *
   * *
  *****
 *     *
*       *
'''
## template
n = int(input())
mid = n // 2 + 1
res = [[' '] * (n + mid*2 - 2 ) for _ in range(n + 1)]
res[1][n - 1] = '*'
point = n-1
a= point -1
b = point+1
for i in range(2,mid):
    res[i][a]='*'
    res[i][b]='*'
    a-=1
    b+=1
    point
for i in range(a,b+1):
    res[mid][i]='*'
a-=1
b+=1
for i in range(mid+1,n+1):
    res[i][a]='*'
    res[i][b]='*'
    a-=1
    b+=1
for j in range(1,n+1):
    for i in res[j]:
        print(i,end='')
    print()



