graph = [[0]*101 for _ in range(101)]
n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]
for _ in range(n):
    x,y,d,g = map(int, input().split())
    graph[y][x]=1

    #드래곤 커브 만들기 --> 이게 핵심이다
    dragon = [d]
    for _ in range(g):
        for a in range(len(dragon)-1,-1,-1):
            dragon.append((dragon[a]+1)%4)

    #좌표 찍어나가기
    for d in dragon:
        x+=dx[d]
        y+=dy[d]
        # 제한 조건 : 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
        # 위 제한 조건에 의해 밑에 코드는 없어도 된다
        # if 0<=x<101 and 0<=y<101 and graph[y][x]==0:
        graph[y][x]=1

# 사각형 개수 구하기
answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i][j+1]==1 and graph[i+1][j]==1 and graph[i+1][j+1]==1:
            answer+=1

print(answer)