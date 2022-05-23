"""
import sys
sys.stdin=open("input.txt","rt")
"""
n ,k= map(int,input().split())

buffer=[]
for i  in range(1,n+1):
    if(n%i == 0):
        buffer.append(i)
    else:
        continue
if(len(buffer)<k):
    print(-1)
else:
 print(buffer[k-1])







