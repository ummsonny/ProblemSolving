n = int(input())

array = list(map(int, input().split()))
visit = [1]*n

maxValue = -1e9

sum_array = []

def operation(sum_array):

    summary = 0
    for i in range(n-1):
        summary += abs(sum_array[i]-sum_array[i+1])

    return summary

def dfs(count):
    global maxValue

    if count == n:
        summary = operation(sum_array)
        maxValue = max(maxValue, summary)

    for i in range(n):
        if visit[i] == 1:
            count +=1
            visit[i] =0
            sum_array.append(array[i])
            dfs(count)
            count -=1
            visit[i]=1
            sum_array.pop()

dfs(0)
print(maxValue)
