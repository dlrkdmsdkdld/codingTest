'''
https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
 kmp 알고리즘 설명 사이트 
입력

2
ababa
aba
abracadabra
ab
출력
#1 2
#2 2
'''

def KMPSearch(pat, txt):
    global cnt
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    # Preprocess the pattern
    computeLPS(pat, lps)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # Pattern을 찾지 못한 경우
        elif pat[j] != txt[i]:
            # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j-1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # Pattern을 찾은 경우
        if j == M:
            cnt+=1
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = lps[j-1] # 검색 문자열 자체에서의 패턴을 찾아서 얼마나 겹치는지 알수있음  예를들어 aba일때 txt에서 aba를 찾았으면 다음 i 번째 부터 찾을때 무조건 a부터시작한다
def computeLPS(pat, lps):
    leng = 0  # length of the previous longest prefix suffix
    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(input())
    findStr = input()
    find = list(findStr)
    tmp = ''
    cnt = 0
    step = 0
    findNum = len(find)
    n = len(data)
    lps=[0]*(n)
    KMPSearch(find,data)
    print("#{} {}".format(test_case, cnt))