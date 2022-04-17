#상어 move()에서 이동시키면서 떠나온 전 자리를 0으로 초기화 해줘야한다.
#또한 move()에서 반복문이 돌아가면서 이전에 처리한 상어를 또 처리하지 않기위해
#visited를 도입했다. --> 나동빈은 이 모든걸 새로운 배열 new_array로 해결함
from collections import deque

n,m,k = map(int, input().split())

array=[]

for i in range(n):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0,0]]*n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def update_smell(): #상어들이 움직이고 난 후 업데이트

    for i in range(n):
        for j in range(n):
            #냄새가 존재하는 경우
            if smell[i][j][1] > 0:
                smell[i][j][1]-=1
            #상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

def move():

    #new_array = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):

            if array[x][y] != 0 and visited[array[x][y]-1] == 0: #상어 있다면
                
                visited[array[x][y]-1] = 1
                direction = directions[array[x][y]-1]
                found = False

                #1. 다른 상어 냄새가 존재하지 않는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]

                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][1] == 0:
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]

                            if array[nx][ny] == 0: #다른 상어가 없으면
                                array[nx][ny] = array[x][y]
                            else: #다른 상어가 있으면
                                array[nx][ny] = min(array[nx][ny], array[x][y])
                            
                            array[x][y] = 0
                            found = True
                            break
                if found:
                    continue

                #2. 갈곳못찾아서 다시 내 냄새로 돌아가야함

                for index in range(4):
                    nx = x + dx[priorities[array[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[array[x][y]-1][direction-1][index]-1]

                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][0] == array[x][y]: #내 냄새라면
                            directions[array[x][y]-1] = priorities[array[x][y]-1][direction-1][index]

                            array[nx][ny] = array[x][y]
                            array[x][y]=0
                            break


time = 0
while True:
    visited = [0] * m
    update_smell()
    move()
    time+=1

    #1번만 살아남았는지 체크
    check = True

    for i in range(n):
        for j in range(n):
            if array[i][j]>1:
                check = False

    if check:
        print(time)
        break

    if time>=1000:
        print(-1)
        break