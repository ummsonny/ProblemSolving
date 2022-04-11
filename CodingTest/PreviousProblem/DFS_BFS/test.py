'''
파이썬은 함수 안에만 지역변수임 while이나 for문에서는 global변수쓰는거임 
'''
x=2
while True: 

    #node, s, x, y = (1,1,1,1)
    x =1
    break

print(x)

a = 10  # 전역변수
def func(): 
    a = 20 # 지역변수 
    print(f"2. {a}") 
    return a + 100 # 여기서의 a는 바로위 지역변수 a

print(f"1. {a}") 
print(f"3. {func()}") # func() 함수가 호출되고 끝나면 func() 내부 지역변수가 살았다가 사라짐

