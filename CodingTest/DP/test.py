from collections import deque
graph = [[0,1,1,0,1,1,1],
        [0,1,1,0,1,1,1],
        [1,1,0,0,1,1,1],
        [1,1,0,0,0,0,0],
        [1,1,1,1,1,0,0]]
dx = [1,1,0]
dy = [0,1,1]
answer = ''
def make(x,y,n,m):
    global answer

    visit = [[0]*m for _ in range(n)]
    q = deque([(0,x,y)])
    visit[x][y]=1
    flag = 0

    while q:

        cost,a,b = q.popleft()

        for i in range(3):
            nx,ny = a+dx[i], b+dy[i]

            if not(0<=nx<n and 0<=ny<m):
                flag = cost+1
                break

            if visit[nx][ny]==0:
                if graph[nx][ny]==graph[x][y]:
                    visit[nx][ny]=1
                    q.append((cost+1,nx,ny))
                else:
                    flag = cost+1
                    break
        
        if flag:
            break
        
    for r in range(x,x+flag):
        for c in range(y,y+flag):
            check[r][c]=1
    if flag>1:
        answer += (str(graph[x][y])+str(flag))
    else:
        answer += str(graph[x][y])
    return

n = len(graph)
m = len(graph[0])
check = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not check[i][j]:
            make(i,j,n,m)

print(answer)

