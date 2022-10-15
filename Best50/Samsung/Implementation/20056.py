# 파이어볼의 번호는 중요하지 않다!

n,m,k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

fireball = []

for _ in range(m):
    fireball.append(list(map(int, input().split())))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for _ in range(k):
    #구슬 이동
    while fireball:
        a,b,c,d,e = fireball.pop(0)
        nx = (a + d * dx[e]) % n
        ny = (b + d * dy[e]) % n
        graph[nx][ny].append(([c,d,e]))

    #2개 이상인지 체크
    for x in range(n):
        for y in range(n):
            length = len(graph[x][y])
            if length>1:
                sum_m,sum_s,cnt_odd,cnt_even,cnt = 0,0,0,0,length
                while graph[x][y]:
                    m,s,d = graph[x][y].pop(0)
                    sum_m += m
                    sum_s += s
                    if d%2 == 0:
                        cnt_even+=1
                    elif d%2 != 0:
                        cnt_odd +=1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                if sum_m//5: #질량이 0이 아니라면
                    for d in nd:
                        fireball.append([x, y, sum_m//5, sum_s//cnt, d])

            if length == 1:
                fireball.append([x,y]+graph[x][y].pop())

answer = 0

for i in fireball:
    answer+=i[2]

print(answer)

'''
문제 풀이 팁
1.
처음 그래프 상태(deque로 표현) -> 이동 후 그래프(graph로 표현) -> 파이어볼 변신 후 그래프(deque로 표현)
2.(이건 아직 안해봄)
처음 그래프 상태(graph이용) -> 이동 후 그래프(temp_graph로 표현) -> 파이어볼 변신 후 그래프(temp_graph를 graph에 대입)

위 두가지 방법은 비슷하나 처음 및 마지막 변신 후 즉, 상태 변화가 완료된 그래프를 deque로 관리하냐 아님 graph로 이용하냐의 차이이다.
공통점은 1은 graph로 2는 temp_graph로 추가적인 공간을 둔다는 것이다.
즉, 미세먼지 안녕이나 이 문제처럼 볼의 이동이던지, ***"동시에"*** 모든 칸에서 어떤 변화가 일어나면 이 변화를 담아둘 공간을 추가로 만들자!!!!!!!!
'''

# ==========================================================#

# fireball과 graph의 원소를 튜플로 한 것
from collections import deque
n,m,k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]
fireball = deque([])
for _ in range(m):
    r,c,m,s,d = map(int, input().split())
    fireball.append((r-1,c-1,m,s,d))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def move():

    while fireball:
        x,y,m,s,d = fireball.popleft()
        nx = (x+dx[d]*s)%n
        ny = (y+dy[d]*s)%n
        graph[nx][ny].append((m,s,d))

def transform():
    for i in range(n):
        for j in range(n):
            length = len(graph[i][j])
            if length>=2:
                gm,gs,count = 0,0,0
                while graph[i][j]:
                    m,s,d = graph[i][j].pop()
                    gm+=m
                    gs+=s
                    if d%2!=0:
                        count+=1
                    else:
                        count-=1
                if gm//5==0:
                    continue

                if abs(count)==length:
                    for k in range(4):
                        fireball.append((i,j,gm//5,gs//length,k*2))
                else:
                    for k in range(4):
                        fireball.append((i,j,gm//5,gs//length,k*2+1))
            elif length == 1:
                m,s,d = graph[i][j].pop()
                fireball.append((i,j,m,s,d))

for _ in range(k):

    # 이동
    move()

    # 2개 이상의 파이어볼이 있는 칸에서 변화
    transform()


answer = 0
for x,y,m,s,d in fireball:
    answer += m

print(answer)