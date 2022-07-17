'''
조합 구하기
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑는 방법의 수를 출력하는 프로그
램을 작성하세요.
▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.
▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.
▣ 입력예제 1
4 2
▣ 출력예제 1
1 2
1 3
1 4
2 3
2 4
3 4
6

'''

def DFS(L,data,k):
    global cnt
    if L==m:
        cnt+=1
        for i in data:
            print(i,end=' ')
        print()
    else:
        for i in range(k,n+1):
            if ch[i]==0:
                data.append(i)
                ch[i]=1
                DFS(L+1,data,i)
                ch[i]=0
                data.pop()
if __name__ == '__main__':
    n,m=map(int,input().split())
    cnt=0
    ch=[0]*(n+1)
    d=[]
    DFS(0,d,1)
    print(cnt)


