n = int(input())
array = list(map(int, input().split()))
array.sort()
# print(array)

result=0 # 그룹의 수
count=0 # 현재 그룹에 포함된 모험가 수

for i in array:
    count+=1
    if count>=i: # 사람 수 >= 공포도
        result+=1
        count=0

print(result)

#오름차순으로 보면서 계속 최소한의 모험가 수만 포함하면 바로 그룹만들어서 빼버리므로 정당성이 확보된다.