import sys



#내 좆같은 풀이
# n = int(sys.stdin.readline())

# arr = {}
# for i in range(n):
#     a = sys.stdin.readline();
#     if a in arr:
#         arr[a]+=1
#     else:
#         arr[a]=1
# maxv = 0
# maxk = 'hi'
# for key in arr.keys():
#     if maxv<arr[key]:
#         maxv=arr[key]
#         maxk = key
#     elif maxv==arr[key] and int(maxk)>int(key):
#         maxk=key

#개선된 풀이
n = int(sys.stdin.readline())

arr = {}
for i in range(n):
    a = int(sys.stdin.readline());#그냥 정수형도 key가 될 수 있다.
    if a in arr:
        arr[a]+=1
    else:
        arr[a]=1
answer = sorted(arr.items(), key = lambda x:(-x[1], x[0]))#리스트의 원소가 튜플이던 배열디너 뭐 던 lambda만 잘 해주면 됨 여기는 튜플임

print(answer[0][0])