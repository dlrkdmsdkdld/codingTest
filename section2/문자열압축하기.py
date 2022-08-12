## template
'''
문자열압축
입력예제
AAABBBBC

출력
3A3BC
'''
d = list(input())
res = []
last = d.pop(0)
step = 1
while d:
    tmp = d.pop(0)
    if last == tmp:
        step += 1
    else:
        if step == 1:
            res.append(last)
            step = 1
        else:
            res.append(step)
            res.append(last)
            step = 1

    last = tmp
    if not d:
        if step == 1:
            res.append(tmp)
            step = 1
        else:
            res.append(step)
            res.append(tmp)
            step = 1

for i in res:
    print(i, end='')

