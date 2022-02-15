n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0]*m for _ in range(n)] # 벽을 세운뒤 맵

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

result = 0

def virus(x,y): # 바이러스 퍼짐 by DFS
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if temp[nx][ny] == 0:
                temp[nx][ny]=2
                virus(nx, ny)

def get_score(): # 안전한 장소 찾기
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score+=1
    return score

#dfs를 이용해서 벽 만들기! & 매번 안전 영역 계산

def dfs(count): # 내가 이전에 생각한 dfs랑 좀 다른 유형의 dfs **********
    global result

    if count == 3: # dfs가 무한대로 깊어지지 않기 위한 조건문
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)

        result = max(result, get_score())
        return

    # dfs시작
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1 # 들어온 매개변수값의 수정이 가능함? 신기하네
                dfs(count)
                data[i][j]=0
                count-=1

dfs(0)
print(result)

    