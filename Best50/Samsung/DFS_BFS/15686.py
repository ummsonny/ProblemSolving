n,m = map(int, input().split())

graph = []
home = []
restaurant = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        if graph[i][j] == 2:
            restaurant.append((i,j))

length = len(restaurant)
choice = []

global_distance = 1e9
def dfs(count, start):
    global global_distance

    if count == m:
        global_distance = min(global_distance, city_distance())
        return

    for i in range(start, length):
        choice.append(restaurant[i])
        dfs(count+1, i+1) # 여기가 핵심 !!!! 조합!!!!!! start가아니라 i가 들어가야함
        choice.pop()

def city_distance():

    answer = 0
    for a,b in home:
        summary = 1e9
        for i, j in choice:
            summary = min(summary, abs(a - i) + abs(b - j))
        answer += summary

    return answer

dfs(0,0)
print(global_distance)
