# 섹션 1 - 1부터 N까지 홀수 출력하기
'''
n = int(input())
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)
    else:
        continue
   '''
# 섹션 1 - 1부터 N까지 합 출력하기
'''
n = int(input())
k=0
for i in range(1, n+1):
    k =k+ i

print(k)
'''
# 섹션 1 - N의 약수 출력하기
n = int(input())
for i in range(1 , n+1):
    if n%i == 0:
        print(i , end=' ')
    else:
        continue


