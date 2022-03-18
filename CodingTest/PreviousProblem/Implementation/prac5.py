n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b]=1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x), c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction    

def simulate():

    x,y = 1, 1 #뱀 머리
    data[x][y] = 2 #뱀이 있는 곳은 2
    direction = 0 #처음에는 동쪽을 보고 있음
    time = 0
    index = 0 #다음 회전할 정보 즉 회전할 타이밍(초) info에 쓰일꺼임
    q = [(x,y)] #뱀이 차이자하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1<=nx and nx<=n and 1<=ny and ny<=n and data[nx][ny]!=2:
            
            #사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py]=0

            #사과가 있다면 이동 후에 꼬리 그래도 두기
            if data[nx][ny] == 1:
                data[nx][ny]=2
                q.append((nx,ny))

        else: # 벽 부딫히거나 자기 몸이랑 만남
            time+=1
            break

        x,y = nx, ny
        time+=1
        if index < l and time == info[index][0]: # 1이 아니라 l소문자이다.
            direction= turn(direction, info[index][1])
            index+=1
    return time

print(simulate())