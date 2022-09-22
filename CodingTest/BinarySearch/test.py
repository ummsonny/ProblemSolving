from unittest import result


n,m = map(int, input().split())
array = list(map(int, input().split()))


def binary_search(array,target,start,end):
    result=0
    while start<=end:
        mid = (start+end)//2

        su = 0
        for i in array:
            if i>mid:
                su+=(i-mid)
        
        if su<target:
            end = mid-1
        else:
            result = mid
            start=mid+1
    return result

print(binary_search(array,m,0,max(array)))
