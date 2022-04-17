n,m = map(int, input().split())

arr = list(map(int, input().split()))
visit = [1]*n

max_value=-1e9
def dfs(count, summary):
    global max_value

    if count == 3:
        if max_value<summary<=m:
            max_value = summary
        return

    for i in range(n):
        if visit[i]==1:
            visit[i]=0
            dfs(count+1, summary+arr[i])
            visit[i]=1

dfs(0,0)
print(max_value)