
data = input()
res = []
for i in data:
    res.append(i)

# print(res)
st = []
cnt=0
while res:
    k=res.pop(0)
    if k=='(' and res[0] ==')':
        res.pop(0)
        cnt+=len(st)
        continue
    elif k==')':
        cnt+=1
        st.pop()
    else:
        st.append('(')

print(cnt)
