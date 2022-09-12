## template
'''
임의의 자연수는 그보다 작은 자연수들의 합으로 표현될 수 있다. 예를 들어 4의 경우,

4
= 3+1
= 2+2
= 2+1+1
= 1+1+1+1

위와 같은 방법으로 표현 될 수 있다. 이 때 , 숫자의 구성이 같으면서 그 순서만이 다른 경우는 같은 경우로 생각하는데, 예를 들어 다음 세 가지 경우는 모두 같은 경우이다.

2 + 1 + 1, 1 + 2 + 1 , 1 + 1 + 2

자연수 n을 입력 받아 이를 n보다 작은 자연수들의 합으로 나타내는 방법을 모두 출력하는 프로그램을 재귀 호출을 사용하여 작성하시오.



'''
def DFS(data, L):
    global cnt
    global k
    result = sum(data)
    if result > k:
        return
    if result == k:
        cnt += 1
        for z in range(0, len(data)):
            if z != len(data) - 1:
                print(data[z], end="+")
            else:
                print(data[z], end="")
        print()


    else:
        for i in range(L, 0, -1):
            if result + i <= k:
                data.append(i)
                DFS(data, i)
                data.pop()


if __name__ == '__main__':
    k = int(input())
    cnt = 0
    DFS([], k - 1)
    print(cnt)
