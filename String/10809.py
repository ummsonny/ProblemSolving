#내 풀이
n = input()

arr = [-1]*26

for i in range(len(n)):
    if arr[ord(n[i])-97]==-1: #-1이 아니라면 어차피 앞에서 나온거니까 걍 넘어가고 -1일때만 고려!
        arr[ord(n[i])-97]=i

for i in range(26):
    print(arr[i],end=' ')

#파이썬의 장점 활용

n = input()

arr = [-1]*26

for i in range(len(n)):
    arr[ord(n[i])-97]=n.find(n[i]) #문자열에서 가장 앞에 있는 문자의 위치를 나타낸다. find!!!!

for i in range(26):
    print(arr[i],end=' ')