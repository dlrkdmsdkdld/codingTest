## template
dx = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def dfs(x, y):
  ok =True
  tmp = []
  res=data[x][y]
  total = [ data[x][y] ]
  for i in dx:
    xx= x+i[0]
    yy=y+i[1]
    if 0<=xx<n and 0<=yy<n and data[xx][yy] not in total:
      if data[xx][yy] not in total:
        total.append(data[xx][yy])
        tmp.append((xx+i[0],yy+i[1] , i[0],i[1])  )
        res+=data[xx][yy]
      else:
        tmp.append((xx+i[0],yy+i[1] , i[0],i[1])  )

    else:
      ok =False
      break
  if ok==True:
    while tmp:
      fc = tmp.pop(0)
      if 0<=fc[0]<n and 0<=fc[1]<n :
        if data[fc[0]][fc[1]] not in total:
          total.append(data[fc[0]][fc[1]])
          res += data[fc[0]][fc[1]]
          tmp.append(  (fc[0]+fc[2] , fc[1]+fc[3],fc[2],fc[3]  )   )
        else:
          tmp.append(  (fc[0]+fc[2] , fc[1]+fc[3],fc[2],fc[3]  )   )
    return res
  else:
    return 0

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
      data = []
      n = int(input())
      for z in range(n):
        tmp = list(map(int,input().split()))
        data.append(tmp)

      maxres=0
      for i in range(0,n):
        for j in range(0,n):
          k = dfs(i,j)
          if k >maxres:
            maxres=k
      print("#{} {}".format(tc+1,maxres))




