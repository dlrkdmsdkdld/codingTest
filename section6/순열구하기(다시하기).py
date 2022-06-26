import  sys
'''
순열 구하기
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 
출력합니다.
▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.
▣ 입력예제 1 
3 2
▣ 출력예제 1
1 2
1 3
2 1
2 3
3 1
3 2
6



'''
def DFS(L):
    global cnt
    if L==m:
        cnt+=1
        for i in res:
            print(i,end=' ')
        print()

    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L + 1)
                ch[i]=0


if __name__ == '__main__':
    n ,m=map(int,input().split())
    cnt=0
    res=[0]*m
    ch=[0]*(n+1)
    DFS(0)
    print(cnt)

