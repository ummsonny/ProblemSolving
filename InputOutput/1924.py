month = [31,28,31,30,31,30,31,31,30,31,30,31]

m, d = map(int, input().split())

days = sum(month[:m-1])+d #여기가 핵심이다!!*** 여기 개쩔었다.


#print(month[:m-1]) 
# ty = "sefalsd;kfjaiosejf"
# print(ty[0:0]) 
# 리스트[b:b]라면 아무것도 안된다.
#리스트[0:0]이라면 0에서 -1까지니까 문자열 전체구나라고
#오해 할 수 있는데 아니다. 그냥 아무것도 아님 
#but 리스트[0:-1] 는 0에서 -2까지 문자열 슬라이싱 가능


if days%7==1:
    print("MON")
elif days%7==2:
    print("TUE")
elif days%7==3:
    print("WED")
elif days%7==4:
    print("THU")
elif days%7==5:
    print("FRI")
elif days%7==6:
    print("SAT")
else:
    print("SUN")

# Day = 0
# arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"] 이걸 쓰면 조건문 안써도 된다.
 
# x, y = map(int,input().split())
 
# for i in range(x-1):
#     Day = Day + arrList[i] 내 코드 5번째 줄로 대체 가능 
# Day = (Day + y) % 7
 
# print(weekList[Day])