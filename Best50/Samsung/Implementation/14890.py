n,l = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def row_check(x,y,check):

    while y<n:

        nx,ny = x,y+1

        #끝에 도착!
        if ny>=n:
            return True
        #높이 차이가 2이상이면 실패!
        if abs(graph[nx][ny]-graph[x][y])>=2:
            return False
        #전진
        if graph[nx][ny]==graph[x][y]:
            x,y = nx,ny
            continue
        else:
            if graph[nx][ny]>graph[x][y]:
                height = graph[x][y]
                for i in range(0,l):
                    mx,my = x,y-i
                    if not(0<=my<n and check[mx][my]==0 and graph[mx][my]==height):
                        return False
                    else:
                        check[mx][my]=1
            else:
                height = graph[nx][ny]
                for i in range(0,l):
                    mx,my = nx,ny+i
                    if not(0<=my<n and check[mx][my]==0 and graph[mx][my]==height):
                        return False
                    else:
                        check[mx][my]=1
            x,y = nx, ny
def column_check(x,y,check):

    while x<n:

        nx,ny = x+1,y

        #끝에 도착!
        if nx>=n:
            return True
        #높이 차이가 2이상이면 실패!
        if abs(graph[nx][ny]-graph[x][y])>=2:
            return False
        #전진
        if graph[nx][ny]==graph[x][y]:
            x,y = nx,ny
            continue
        else:
            if graph[nx][ny]>graph[x][y]:
                height = graph[x][y]
                for i in range(0,l):
                    mx,my = x-i,y
                    if not(0<=mx<n and check[mx][my]==0 and graph[mx][my]==height):
                        return False
                    else:
                        check[mx][my]=1
            else:
                height = graph[nx][ny]
                for i in range(0,l):
                    mx,my = nx+i,ny
                    if not(0<=mx<n and check[mx][my]==0 and graph[mx][my]==height):
                        return False
                    else:
                        check[mx][my]=1
            x,y = nx, ny

answer = 0
check = [[0]*n for _ in range(n)]
for i in range(n):
    if row_check(i,0,check):
        answer +=1

check = [[0]*n for _ in range(n)]
for j in range(n):
    if column_check(0,j,check):
        answer +=1

print(answer)

# 다른 사람 풀이
# 여기는 행/열 각각 배열을 만들어서 함수에 넘겨줘서 코드를 더 짧게 했다.
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def check_line(line):
    for i in range(1, n): # 두번째 칸부터 체크한게 핵심
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i + j] or slope[i + j]:
                    return False
                if line[i] == line[i + j]:
                    slope[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = True
    return True


for i in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for i in range(n)]):
        ans += 1

print(ans)