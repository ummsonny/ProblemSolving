n = int(input())

array = list(map(int, input().split()))

d = [0]*100

d[0]=array[0]
d[1]=max(array[0], array[1])

for i in range(2, n):
    d[i]= max(d[i-1], d[i-2]+array[i])

print(d[n-1])

'''
여기서 알아둘 점은 i번째 식량창고에 대한 최적의 해를 구할 때 
왼쪽부터 (i - 3)번째 이하의 식량창고에 대한 최적의 해에 대해서는 고려할 필요가 없다는 점이다. 
예를 들어 d[i - 3]는 d[i - 1]과 d[i - 2]을 구하는 과정에서 이미 계산되었기(고려되었기) 때문에, 
d[i]의 값을 구할 때는 d[i - 1]과 d[i - 2]만 고려하면 된다. 따라서~
'''