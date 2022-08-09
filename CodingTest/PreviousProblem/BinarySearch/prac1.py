#1. 함수 정의 풀이법
#  def first(array, target, start, end):
    
#     if start>end:
#         return None
#     mid = (start+end)//2

#     if (mid==0 or target>array[mid-1]) and array[mid]==target:
#         return mid
#     elif array[mid]>=target: # 왜 여기는 >=이고 last()는 > 이냐 찾고자하는 k가 1개만 있으면 모르겠는데 여러개 있자나!
#         return first(array, target, start, mid-1)

#     else:
#         return first(array, target, mid+1, end)

# def last(array, target, start, end):
    
#     if start>end:
#         return None
#     mid = (start+end)//2

#     if (mid==n-1 or target<array[mid+1]) and array[mid]==target:
#         return mid
#     elif array[mid]>target:
#         return last(array, target, start, mid-1)

#     else: #여기는 array[mid]<=target 이다 first 는 < 이다.
#         return last(array, target, mid+1, end)

# def count_by_value(array,x):
#     n = len(array)
#     a = first(array, x, 0, n-1)
#     if a==None: # 이거 못찾으면 걍 없는거자나 그래서 리턴한다.
#         return 0
#     b = last(array, x, 0, n-1)

#     return b-a+1



# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# count = count_by_value(array, x)

# if count==0:
#     print(-1)
# else:
#     print(count)



#2. 라이브러리 사용법
from bisect import bisect_left, bisect_right

def count_by_value(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index
    
n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)