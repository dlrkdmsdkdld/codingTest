"""
[입력]

첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
각 테스트 케이스는 다음과 같이 구성되었다.
첫 번째 줄에 정수 N, M이 주어진다. (1 ≤ N ≤ 30 , 0 ≤ M ≤ 108)



[출력]

각 테스트 케이스마다 한 줄씩

마지막 N개의 비트가 모두 켜져 있다면 ON

아니면 OFF 를 출력하라.
입력
5
4 0
4 30
4 47
5 31
5 62
출력
#1 OFF
#2 OFF
#3 ON
#4 ON
#5 OFF
"""
T = int(input())
data=[]
for i in range(0,T):
    x,y=map(int,input().split())
    data.append((x,y))
for test_case in range(1, T + 1):
    tmp = data.pop(0)
    k=tmp[0]
    m=tmp[1]
    tmp=[]
    while m>1:
        if m%2==0:
            tmp.insert(0,0)
        else:
            tmp.insert(0,1)
        m=m//2
    if m==1:
        tmp.insert(0,1)
    else:
        tmp.insert(0,0)
    button=0
    if len(tmp) <k:
        button = 1
        print("#{}".format(test_case), "OFF")
    else:
        a=len(tmp)-1
        for i in range(a,a-k,-1):
            if tmp[i]==0:
                print("#{}".format(test_case),"OFF")
                button=1
                break
    if button==0:
        print("#{}".format(test_case),"ON")


