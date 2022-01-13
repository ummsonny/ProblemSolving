n, m = map(int, input().split())

#방문 위치를 저장하기 위해 맵을 생성하여 0으로 초기화
visited = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
visited[x][y] = 1 #현재 좌표 방문 처리해야지! 

#입력된 맵 생성
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
array = [list(map(int, input().split())) for _ in range(n)]

#북동남서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction<0:
        direction=3

#이제 구현
count =1 #방문한 칸 수
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny]==0 and array[nx][ny]==0:#갈 곳이 있다.
        visited[nx][ny]=1
        x = nx
        y = ny
        count+=1
        turn_time=0
        continue
    else: # 아직 다른 방향을 더 봐야 겠다
        turn_time+=1

    if turn_time==4: # 한 바퀴 다 돌았는데 이미 방문했거나 바다여서 갈 곳이 없다!
        nx = x-dx[direction]
        ny = y-dy[direction]

        if array[nx][ny]==0: # 뒤로 갈 수 있다면 빠꾸 즉, 육지라면 빠꾸
            x = nx
            y = ny
        else:
            break
        turn_time=0

print(count)
