from collections import deque
n,m,k = map(int, input().split())
winter = []
for _ in range(n):
    winter.append(list(map(int, input().split())))

yang = [[5]*n for _ in range(n)]
tree = [[deque([]) for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y,age = map(int, input().split())
    tree[x-1][y-1].append(age) # 나이

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for _ in range(k):
    #spring&summer
    for i in range(n):
        for j in range(n):
            length = len(tree[i][j])
            for k in range(length):
                if yang[i][j]-tree[i][j][k]>=0:
                    yang[i][j]-=tree[i][j][k]
                    tree[i][j][k]+=1
                elif yang[i][j]-tree[i][j][k]<0:
                    for _ in range(k,length): # 이 부분이 문제 풀이의 핵심이다! 양분 없으면 바로 나무들 양분 만들어 버리기
                        yang[i][j]+=(tree[i][j].pop()//2)
                    break

    #가을
    temp = [[deque([]) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for t in tree[i][j]:
                if t%5==0:
                    for d in range(8):
                        ni,nj = i+dx[d],j+dy[d]
                        if 0<=ni<n and 0<=nj<n:
                            temp[ni][nj].appendleft(1)
                    temp[i][j].append(t)
                else:
                    temp[i][j].append(t)
    tree = temp

    #겨울
    for i in range(n):
        for j in range(n):
            yang[i][j]+=winter[i][j]
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)



# 밑에는 시간초과 나지만 deque로 푼 좋은 아이디어여서 남겨놓은것이다.
'''
from collections import deque
n,m,k = map(int, input().split())
winter = []
for _ in range(n):
    winter.append(list(map(int, input().split())))

yang = [[5]*n for _ in range(n)]
trees = deque([])

for _ in range(m):
    x,y,age = map(int, input().split())
    trees.append([age,x-1,y-1]) #(나이,x,y)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for o in range(k):
    #spring&summer 양분먹고 나이 증가 OR 못먹고 바로 양분
    #큐가 만약 오름차순으로 있다면 popleft() -> append()해도 계속 오름차순 유지
    length = len(trees)
    dead_tree = []
    for _ in range(length):
        tree = trees.popleft()
        age,x,y = tree[0], tree[1], tree[2]
        if yang[x][y]-age>=0: # 나이증가 경우
            yang[x][y]-=age
            trees.append([age+1,x,y])
        elif yang[x][y]-age<0: # 양분 되는경우
            dead_tree.append((age,x,y))
    for age,x,y in dead_tree:
        yang[x][y] += age//2

    #가을 - 번식
    temp = []
    for tree in trees:
        if tree[0]%5==0:
            for d in range(8):
                ni,nj = tree[1]+dx[d],tree[2]+dy[d]
                if 0<=ni<n and 0<=nj<n:
                    temp.append([1,ni,nj])
    trees = deque(temp+list(trees))

    #겨울 - 양분 더 뿌려줌
    for i in range(n):
        for j in range(n):
            yang[i][j]+=winter[i][j]


answer = len(trees)
# print(answer)
'''