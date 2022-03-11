data = input()
count0 = 0 # 모두0만드는데 횟수
count1 = 0 # 모두1만드는데 횟수

if data[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i]!=data[i+1]: # 달라지는 부분 찾는 스킬
        if data[i+1]=='1':
            count0+=1
        else:
            count1+=1

print(min(count0, count1))
