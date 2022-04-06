n, m = map(int, input().split())
x,y,d = map(int, input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d-=1
    if d<0:
        d=3

count = 1
turn_time=0
while True:

    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if graph[nx][ny]==0:
        graph[nx][ny]=2
        x,y = nx, ny
        turn_time=0
        count+=1
        continue

    else:
        turn_time+=1

    if turn_time==4:
    
        nx = x - dx[d]
        ny = y - dy[d]

        if graph[nx][ny]==0:
            x,y = nx, ny
        else:
            break
        turn_time=0

print(count)



