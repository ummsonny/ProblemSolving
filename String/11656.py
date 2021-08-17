n = input()
arr =[]
for i in range(len(n)):
    arr.append(n[i:])# 핵심!!!!!!!!!
for i in sorted(arr):
    print(i)