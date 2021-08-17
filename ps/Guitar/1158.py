n, k = map(int, input().split())
arr = list(range(1,n+1))
ans = []
idx = 0

for i in range(n):
    idx += k-1

    if idx>=len(arr):
        idx %=len(arr)
    
    ans.append(str(arr.pop(idx))) #그냥 파이썬에는 문자형 없다고 생각해라 무조건 문자열형! str!!

print("<"+', '.join(ans)+'>') # join(list)의 list는 문자(열)로된 list만 가능!!!! (문자(열)이라고 했지만 'a' 이것도 문자가 아니라 문자열이다.)
    