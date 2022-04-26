from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(start_x,start_y,group_color,rainbow_list): #시작노드는 일반

    q = deque([(start_x, start_y)])
    visit[start_x][start_y] = group_color

    count = 1
    rainbow_count = 0

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 and graph[nx][ny] != -1:
                if graph[nx][ny] == graph[start_x][start_y]:
                    q.append((nx,ny))
                    visit[nx][ny] = group_color
                    count+=1
                elif graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visit[nx][ny] = group_color
                    count+=1
                    rainbow_count+=1
                    rainbow_list.append((nx,ny))

    for a,b in rainbow_list:
        visit[a][b]=0

    return count, rainbow_count

'''
1. 이 global_rainbow_list가 핵심 --> https://www.acmicpc.net/board/view/74924
위 링크처럼 무지개 가 겹치는 경우도 처리 해줘야 하므로 
'''
global_rainbow_list = []
def find_block():
    global max_leader, global_rainbow_list

    color = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=1 and visit[i][j]==0:

                rainbow_list = []
                color+=1 #그룹 식별별
                a,b = bfs(i,j,color,rainbow_list) #그룹 1개 생성

                '''
                2. 여기 조건문 핵심 
                if ~~:
                elif A:
                    if ~~~: # A가 조건이 맞아서 여기 if문이 실행 되는데 여기 if문이 거짓이라 elif A를 나가게 되도 elif B로 가지 않는다!!!! 그래서 if-else가 아닌 if-if로 코드 작성함
                elif B
                '''
                if max_leader[1]<a:
                    max_leader = [(i,j),a,b]
                    global_rainbow_list = rainbow_list
                if max_leader[1]==a:
                    if max_leader[2]<b:
                        max_leader = [(i,j),a,b]
                        global_rainbow_list = rainbow_list
                if max_leader[1]==a and max_leader[2] == b:
                    if max_leader[0][0]<i:
                        max_leader = [(i, j), a, b]
                        global_rainbow_list = rainbow_list
                    elif max_leader[0][0]==i:
                        if max_leader[0][1]<j:
                            max_leader = [(i, j), a, b]
                            global_rainbow_list = rainbow_list

def remove_block(x,y):

    graph[x][y] = -10

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            if visit[max_leader[0][0]][max_leader[0][1]]==visit[nx][ny] or (nx,ny) in global_rainbow_list:
                if graph[nx][ny] >= 0:
                    remove_block(nx,ny)

#중력 작용
def do_gravity(): #graph를 밑에서 수정해줘야 나중에 또 안만난다.

    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j] >-1:
                r = i

                while True:
                    if 0<=r+1<n and graph[r+1][j]==-10:
                        graph[r+1][j] = graph[r][j]
                        graph[r][j]= -10
                        r+=1
                    else:
                        break
# 반시계 회전 함수
def rot90(a):
    new_a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-1-j][i] = a[i][j]
    return new_a

score = 0
while True:

    visit = [[0] * n for _ in range(n)]
    max_leader = [(-1, -1), -1, -1]

    find_block()
    if max_leader[1]<2:
        print(score)
        break
    remove_block(max_leader[0][0], max_leader[0][1])
    score += max_leader[1]**2
    do_gravity()
    graph = rot90(graph)
    do_gravity()