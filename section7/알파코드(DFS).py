'''
알파코드(DFS)
철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 그래서 서로 어떻게 암
호화를 할 것인지 의논을 하고 있다.
영희 : 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기
로 하자.
철수 : 정말 바보같은 생각이군!! 생각해 봐!! 만약 내가 “BEAN"을 너에게 보낸다면 그것을 암
호화하면 25114이잖아!! 그러면 이것을 다시 알파벳으로 복원할 때는 많은 방법이 존재하는
데 어떻게 할건데... 이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로
BEAN말고도 5가지나 더 있군.
당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데
얼마나 많은 방법인 있는지 구하세요.
▣ 입력설명
첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길
이는 최대 50이다) 0이 입력되면 입력종료를 의미한다.
▣ 출력설명
입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 그 가지
수도 출력한다. 단어의 출력은 사전순으로 출력한다.
▣ 입력예제 1
25114
▣ 출력예제 1
BEAAD
BEAN
BEKD
YAAD
YAN
YKD
6


'''


def DFS(L,data):
    global cnt
    if L == len(res):
        cnt+=1
        print(data)
    else:
        if L!=len(res)-1 and (res[L+1]== 0 or res[L]==0):
                DFS(L+2,data+chr(res[L]*10+res[L+1]+64))

        else:
            tmp=chr(res[L]+64)
            DFS(L+1,data+tmp)

            if L<len(res)-1 and res[L]*10+res[L+1]<27  :#and res[L+2]!=0
                if L <=  len(res)-3 and res[L+2]==0:
                    return
                else:
                    DFS(L+2,data+chr(res[L]*10+res[L+1]+64))


if __name__ == '__main__':
    k=input()
    res =[]
    cnt=0
    for i in k:
        res.append(int(i))

    DFS(0,'')
    print(cnt)