'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

영준이는 루트가 있는 트리에서 BFS(Breadth First Search)를 하려고 한다.

트리는 1에서 N까지의 번호가 붙은 N개의 노드로 이루어져 있으며, 1이 루트이자 동시에 탐색 시작점이다.

BFS는 큐를 이용하여 탐색을 하는데, 큐의 가장 앞에 있는 노드를 뽑아 탐색을 하고, 탐색을 하는 노드의 자식들을 작은 번호부터 순서대로 큐의 뒤쪽에 넣는 방식으로 탐색이 진행된다.

이것은 컴퓨터에서 실제로 진행되는 방식이 아니고 영준이가 직접 노드를 방문해야 하기 때문에, BFS를 한다면 노드를 방문하는 순서가 정해질 것이고 영준이는 그 순서를 따라 최단거리로 트리를 이동하여 모든 노드를 탐색한다.

영준이는 과연 몇 개의 간선을 지나고 나서야 탐색을 끝 마칠 수 있을까?


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 105)이 주어진다.

두 번째 줄에는 각 노드의 부모정점을 의미하는 N-1개의 자연수가 공백으로 구분되어 주어진다. 1번 노드는 루트이므로 부모가 없어 생략된다.

i-1(2 ≤ i ≤ N)번째로 주어지는 수는 i번 노드의 부모 pi (1 ≤ pi < i)이다. 즉 i번 노드의 부모의 번호는 i보다 작다.


[출력]

각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

직접 BFS를 하였을 때 지나게 되는 총 간선의 개수를 출력한다.


[예제 풀이]

아래 그림은 첫 번째 테스트 케이스에서 각 노드를 BFS로 방문할 때의 이동 거리를 나타낸다.
'''
def BFS(nowPoint, target, L,CP,a):
    global cnt
    global l
    if ch[target] == 1 or nowPoint == 0:
        return
    if 0<=nowPoint<=n:
        if nowPoint == target:
            ch[target] = 1

            if l[target] > L:
                l[target]  = L
                cnt = nowPoint
                #print(a)
            return
        else:
            tmp = tree[target]
            if tmp == nowPoint:
                a.append(target)
                BFS(target, target, L + 1,CP,a)
                a.pop()
            else:
                if CP[tree[nowPoint]] ==0:
                    CP[tree[nowPoint]]=1
                    a.append(tree[nowPoint])
                    BFS(tree[nowPoint], target, L + 1,CP,a)
                    a.pop()
                for i in range(1,n+1):
                    if tree[i] == nowPoint and CP[i]==0:
                        CP[i]=1
                        a.append(i)
                        BFS(i,target,L+1,CP,a)
                        a.pop()


T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    res = list(map(int, input().split()))
    tree = [0, 0]
    ch = [0] * (n + 1)
    ch[1] = 1
    ch[0] = 1
    for i in res:
        tree.append(i)
    # print(tree)
    l=[1000]*(n+1)
    totalCnt = 0
    cnt=1
    step = 0
    while 0 in ch:
        step+=1
        que= []
        for i in range(2,n+1):
            if tree[i] == step:
                que.append(i)
        # print(que)
        while que:
            a=[]
            c=[0]*(n+1)
            tP = que.pop(0)
            if ch[tP] == 0 :
                BFS(cnt,tP,0,c,a)
        # for i in range(2, n + 1):
        #     a=[]
        #     BFS(i-1, i, 0,a)
    # print(l)
    print("#{} {}".format(test_case,sum(l) - 2000))

'''  ㅣ모범답안
from collections import deque
 
T = int(input())
def checker(a,b):
    while level_node[a] != level_node[b]:
        if level_node[a] < level_node[b]:
            b = parents[b]
        else:
            a = parents[a]
    # level 을 일치햇는데 부모가 다르다면 그위 부모로 가자
    while a != b:
        a = parents[a]
        b = parents[b]
    # 동일시 되는 부모의 레벨을 가져온다
    return level_node[a]
 
 
for test_case in range(1, T + 1):
    node_num = int(input())
    node_list = list( map(int, input().split()))
    tree = [ [] for _ in range(node_num+1) ]
    level_node = [0] * (node_num + 1)
    parents = [0, 0] + node_list
 
    for idx, var in enumerate(node_list):
        idx=idx+2
        tree[var].append(idx)
        level_node[idx] = level_node[parents[idx]] + 1
 
    queue = deque()
    queue.append(1)
    old = 1
    move_value = 0
    while queue:
        visit = queue.popleft()
        # level 일치 시키기
        value = checker(old,visit)
        move_value += level_node[old] + level_node[visit] - 2*value
        for v in sorted(tree[visit]):
            queue.append(v)
        old = visit
        #print(move_value)
    print("#{} {}".format(test_case, move_value))
'''
