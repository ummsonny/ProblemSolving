# 좀더 나은 풀이
n = int(input())

student = []

for _ in range(n*n):
    student.append(list(map(int, input().split())))

graph = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(n*n):

    surround_info = []
    # max,min값을 잡을때는 후보군에 없는 값으로 해야함
    # 만약 마지막 순서 학생을 할 때 갈 곳은 한 자리 밖에 없는데 max_empty값을 0으로 초기화
    # 해놓는다면 밑에 루프를 돌면서 max_x, max_y값이 갱신이 안대서 0,0에 무조건 가게 되있음
    max_x, max_y, max_friend, max_empty = 0, 0, -1, -1
    for x in range(n):
        for y in range(n):
            friend, empty = 0,0
            if graph[x][y]==0:
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:
                            empty +=1
                        elif graph[nx][ny] in student[i][1:]:
                            friend +=1

                if max_friend<friend:
                    max_x = x
                    max_y = y
                    max_friend = friend
                    max_empty = empty

                elif max_friend == friend and max_empty < empty:
                    max_x = x
                    max_y = y
                    max_friend = friend
                    max_empty = empty

    graph[max_x][max_y] = student[i][0]
result = 0
satis_array = [0,1,10,100,1000]

for i in range(n):
    for j in range(n):
        count = 0
        for a,b,c,d,e in student:
            if graph[i][j] == a:
                for z in range(4):
                    nx = i + dx[z]
                    ny = j + dy[z]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny] in [b,c,d,e]:
                        count += 1

        result += satis_array[count]

print(result)

# 내 풀이
'''
n = int(input())

student = []

for _ in range(n*n):
    student.append(list(map(int, input().split())))

graph = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(n*n):

    surround_info = []

    for x in range(n):
        for y in range(n):
            friend, empty = 0, 0
            if graph[x][y]==0:
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:
                            empty +=1
                        elif graph[nx][ny] in student[i][1:]:
                            friend +=1
                surround_info.append((x,y,friend,empty))

    surround_info.sort(key = lambda k: (-k[2], -k[3], k[0], k[1]))
    graph[surround_info[0][0]][surround_info[0][1]] = student[i][0]

result = 0
satis_array = [0,1,10,100,1000]

for i in range(n):
    for j in range(n):
        count = 0
        for a,b,c,d,e in student:
            if graph[i][j] == a:
                for z in range(4):
                    nx = i + dx[z]
                    ny = j + dy[z]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny] in [b,c,d,e]:
                        count += 1

        result += satis_array[count]

print(result)
'''
