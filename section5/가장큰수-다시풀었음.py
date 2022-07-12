



if __name__ == '__main__':
    m,n = map(int,input().split())
    m=str(m)
    res=[]
    cnt = 0
    st=[]
    for i in m:
        res.append(int(i))
    for i in range(0,len(m)):
            for j in range(len(st)-1,-1,-1):
                if st[j] < res[i] and n>0:
                    n-=1
                    st.pop(j)
            st.append(res[i])
    while n!=0:
        n-=1
        st.pop()

    for i in st:
        print(i,end='')