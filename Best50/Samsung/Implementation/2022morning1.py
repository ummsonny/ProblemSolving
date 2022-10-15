n,m,h,k = map(int, input().split()) # 그래프, 도망자위치, 나무, 턴

runner = [[[] for _ in range(n)] for _ in range(n)]
tree = [[0]*n for _ in range(n)]

for _ in range(m):
    x,y,d = map(int, input().split())
    runner[x-1][y-1].append((d-1,0)) # d==0 좌우, d==1 상하
for _ in range(h):
    x,y = map(int, input().split())
    tree[x-1][y-1]=1

dx = [[0,0],[1,-1]]
dy = [[1,-1],[0,0]]

def moverunner():

    temp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if abs(i-cx)+abs(j-cy)<=3:
                if runner[i][j]:
                    for d,dd in runner[i][j]:
                        nx,ny = i+dx[d][dd],j+dy[d][dd]

                        if not(0<=nx<n and 0<=ny<n):
                            dd=(dd+1)%2
                            nx, ny = i + dx[d][dd], j + dy[d][dd]

                        if not(nx==cx and ny==cy): # 술래가 없다면
                            temp[nx][ny].append((d,dd))
                        else:
                            temp[i][j].append((d,dd))
            else:
                if runner[i][j]:
                    for d in runner[i][j]:
                        temp[i][j].append(d)

    return temp

dxc = [-1,0,1,0]
dyc = [0,1,0,-1]
def makeroute():

    # 술래 움직이는 경로 먼저 만들어 주자
    route = [] #위치 및 방향
    route_reverse = []
    cx,cy = n//2,n//2
    d,step = 0,1
    while cx or cy:
        for _ in range(step):
            route.append((cx,cy,d))
            cx,cy = cx+dxc[d],cy+dyc[d]
            route_reverse = [(cx,cy,(d+2)%4)]+route_reverse

            if not cx and not cy:
                break

        d = (d+1)%4
        if d==0 or d==2:
            step+=1

    route += route_reverse
    # print(route)
    return route

route = makeroute()
leng = len(route)

cx,cy = n//2,n//2
answer = 0
for turn in range(1,k+1):

    # 도망자 움직임
    runner = moverunner()

    # 술래 이동
    cx,cy,d = route[turn%leng]

    # 도망자 잡기
    nx,ny = cx,cy
    for _ in range(3):

        if not(0<=nx<n and 0<=ny<n):
            break

        if runner[nx][ny] and tree[nx][ny]==0:
            answer += turn*len(runner[nx][ny])
            runner[nx][ny]=[]

        nx,ny = nx+dxc[d],ny+dyc[d]

print(answer)

#  다른 내풀이 chdir()함수 사용을 잘 했다
n,m,h,k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,d = map(int, input().split())
    graph[x-1][y-1].append(d-1)

tree = [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int, input().split())
    tree[x-1][y-1]=1

# 술래의 방향 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def makeroute():
    route = []
    cx, cy = n // 2, n // 2
    d, step = 0, 1

    while True:
        for _ in range(step):
            route.append((cx, cy, d))
            cx, cy = cx + dx[d], cy + dy[d]

        if not (0 <= cx < n and 0 <= cy < n):
            break

        d = (d + 1) % 4
        if d == 0 or d == 2:
            step += 1

    route = route[:-1]
    route_re = []
    for x, y, d in route[::-1]:
        route_re.append((x + dx[d], y + dy[d], (d + 2) % 4))

    route += route_re

    return route
route = makeroute()
length = len(route)
location = 0


# 도망자의 방향 우하좌상
rdx = [0,1,0,-1]
rdy = [1,0,-1,0]
def chdir(d):
    if d==0:
        return 2
    elif d==1:
        return 3
    elif d==2:
        return 0
    elif d==3:
        return 1
def run():
    temp = [[[] for _ in range(n)] for _ in range(n)]
    sx,sy = route[location][0],route[location][1]
    for i in range(n):
        for j in range(n):
            if abs(i-sx)+abs(j-sy)<=3:
                if graph[i][j]:
                    for r in graph[i][j]:
                        nx,ny = i+rdx[r],j+rdy[r]
                        if not(0<=nx<n and 0<=ny<n):
                            r = chdir(r)
                            nx,ny = i+rdx[r],j+rdy[r]

                        if nx==sx and ny==sy:
                            temp[i][j].append(r)
                        else:
                            temp[nx][ny].append(r)
            else:
                if graph[i][j]:
                    for r in graph[i][j]:
                        temp[i][j].append(r)
    return temp

def catch(step):
    global answer
    cx,cy,d = route[location]

    for _ in range(3):
        if not(0<=cx<n and 0<=cy<n): break
        if graph[cx][cy] and not tree[cx][cy]:
            answer+=len(graph[cx][cy])*step
            graph[cx][cy]=[]
        cx,cy = cx+dx[d],cy+dy[d]

answer = 0
for step in range(1,k+1):

    # 거리가 3 이하인 도망자가 움직인다.
    graph = run()
    location = step%length
    catch(step)

print(answer)