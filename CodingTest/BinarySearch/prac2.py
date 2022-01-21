import re


def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        
        total=0
        for x in array:
            if x>mid:
                total+=(x-mid)
        
        if total < target:
            end = mid-1
        else:
            result = mid # total>=target이면 정답이 될 수 있으므로 저장해놓은다.
            start = mid+1
    return mid

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = binary_search(array, m, 0, max(array))
print(result)