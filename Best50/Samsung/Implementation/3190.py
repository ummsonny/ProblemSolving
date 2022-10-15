from collections import deque
n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]
# 사과
for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1]=2

# 뱀
snake = deque([(0,0)])
graph[0][0]=1


#회전
#딕셔너리 시간복잡도 https://velog.io/@kimwoody/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%99%80-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EC%9D%98-%EC%A3%BC%EC%9A%94-%EC%97%B0%EC%82%B0-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84
l = int(input())
rotate = {}
for _ in range(l):
    sec,c = input().split()
    rotate[int(sec)]=c



dx = [0,1,0,-1]
dy = [1,0,-1,0]
direction = 0

second = 0
while True:

    second+=1

    #몸길이 늘림
    x,y = snake[0][0]+dx[direction],snake[0][1]+dy[direction] #대가리

    # 벽을 만나거나
    if 0>x or x>=n or 0>y or y>=n:
        break
    # 자기를 만나거나
    if graph[x][y]==1:
        break
    # 사과
    #1. 사과를 만나
    if graph[x][y]==2:
        graph[x][y]=1
        snake.appendleft((x,y))
    elif graph[x][y]==0:
        graph[x][y]=1
        snake.appendleft((x,y))
        tailx,taily = snake.pop()
        graph[tailx][taily]=0

    if second in rotate:
        if rotate[second]=='L':
            direction=(direction-1)%4
        else:
            direction=(direction+1)%4

print(second)