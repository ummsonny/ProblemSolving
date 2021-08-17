#슬라이싱!
str = input()
n = len(str)

for i in range(0,n,10):
    print(str[i:i+10])

#print(str[:100]) 문자열이 100보다 짧아도 그냥 문자열 끝까지만 출력한다. 그 이후는 안하는듯 
