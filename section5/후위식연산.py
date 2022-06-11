'''
후위식 연산
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
▣ 입력설명
첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
▣ 출력설명
연산한 결과를 출력합니다.
▣ 입력예제 1
352+*9-
▣ 출력예제 1
12
'''

def cul(a,b,c):
    a=int(a)
    c=int(c)
    if b == '-':
        return a - c
    if b == '*':
        return a *c
    if b == '+':
        return a+c
    if b == '/':
        return a/c
data = input()
a=[]
for i in data:
    a.append(i)
stack = []
result=''
while len(a)!= 1 :
 for i in range(0,len(a)):
    if i>=2 and a[i-1].isdecimal() and a[i-2].isdecimal() and (a[i]=='*' or a[i]=='+'or a[i]=='-'or a[i]=='/'):
        tmp = cul(a[i-2], a[i],a[i-1])
        a.pop(i)
        a.pop(i-1)
        a.pop(i-2)
        a.insert(i-2,str(int(tmp)))
        break

print(int(a[0]))