'''
입력
첫째 줄에는 민혁이가 영수에게 몇 번이나 질문을 했는지를 나타내는 1 이상 100 이하의 자연수 N이 주어진다. 이어지는 N개의 줄에는 각 줄마다 민혁이가 질문한 세 자리 수와 영수가 답한 스트라이크 개수를 나타내는 정수와 볼의 개수를 나타내는 정수, 이렇게 총 세 개의 정수가 빈칸을 사이에 두고 주어진다.



출력
첫 줄에 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력한다.



예제 입력
4
123 1 1
356 1 0
327 2 0
489 0 1
예제 출력
2
'''
n= int(input())
st = []
for i in range(n):
    tmp = list(map(int, input().split()))
    st.append(tmp)
ok = 0
# for i in st:
#   print(i)
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                flag = 1
                for ch in st:
                    strike, ball = 0, 0
                    first = int(ch[0] / 100)
                    second = int((ch[0] / 10) % 10)
                    third = int(ch[0] % 10)
                    if first == i: strike += 1
                    if second == j: strike += 1
                    if third == k: strike += 1

                    if i == second or i == third: ball += 1
                    if j == first or j == third: ball += 1
                    if k == first or k == second: ball += 1

                    if strike != ch[1] or ball != ch[2]:
                        flag = 0

                if flag == 1:
                    # print(i,j,k)
                    ok += 1
print(ok)

