n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
team = [1]*n
# 능력치 구하는 함수
def value():

    summary1 = 0
    summary2 = 0

    for i in range(n-1):
        for j in range(i+1,n):
            if team[i]==team[j]:
                if team[i] == 1:
                    summary1 += (graph[i][j]+graph[j][i])
                else:
                    summary2 += (graph[i][j]+graph[j][i])
    return (summary1,summary2)

#순열 -> 시간초과난다.
'''
result = 1e9
def dfs(count):
    global result
    if count == n//2:
        team1, team2 =  value()
        result = min(result, abs(team1-team2))
        return

    for i in range(n):
        if team[i] == 1:
            team[i]=2
            dfs(count+1)
            team[i]=1
dfs(0)
print(result)
'''

#조합 -> 시간초과 안난다.
result = 1e9
def dfs(count,start):
    global result
    
    if count == n//2:
        team1, team2 = value()
        result = min(result, abs(team1-team2))
        return

    for i in range(start,n):
        if team[i] == 1:
            team[i]=2
            dfs(count+1,i+1)
            team[i]=1
dfs(0,0)
print(result)