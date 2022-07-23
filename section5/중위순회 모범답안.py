def inorder(a):
    if a <=n:
        inorder(a*2)
        print(alp[a],end='')
        inorder(a*2+1)
if __name__ == '__main__':
    n = int(input())
    alp=[0]*(n+1)
    for i in range(n):
        li = list(input().split())
        alp[i+1]=li[1]
    print('#{}'.format(1),end=' ')
    inorder(1)
    print()