n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

for i in sorted(list): #for문에는 in 다음에 배열이 들어간다!
    print(i)

#(nlogn)정렬도 나중에 해바라**************