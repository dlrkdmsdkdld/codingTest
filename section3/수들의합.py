n , m = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0
for i in range(0,n):
    if data[i] == m:
        cnt += 1
        continue
    tmp = data[i]
    for j in range(i+1,n):
         if tmp+data[j]==m:
            cnt +=1
            break
         elif tmp + data[j] >m:
             break
         else:
             tmp +=data[j]

print(cnt)