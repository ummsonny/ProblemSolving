n = int(input())
a_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

result_max = int(-1e9)
result_min = int(1e9)

def solution(count, now):
    global result_max, result_min, add, sub, mul, div

    if count == n:
        result_max = max(result_max, now)
        result_min = min(result_min, now)

    if add>0:
        add-=1
        solution(count+1, now + a_list[count])
        add+=1

    if sub>0:
        sub-=1
        solution(count+1, now - a_list[count])
        sub+=1

    if mul>0:
        mul-=1
        solution(count+1, now * a_list[count])
        mul+=1

    if div>0:
        div-=1
        solution(count+1, int(now / a_list[count]))
        div+=1    

solution(1, a_list[0])

print(result_max)
print(result_min)
    