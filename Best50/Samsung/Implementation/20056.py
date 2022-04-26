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

