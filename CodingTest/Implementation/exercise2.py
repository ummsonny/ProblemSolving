#내 풀이
n = int(input())
count = 0
for i in range(n+1):
    # print(i)
    if i%3!=0 or i==0:
        count+=(3600-5*9*5*9)
        print(1)
    else:
        count+=3600
        print(2)
print(count)

#해설 풀이
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)