# 내풀이
n = input()

arr = [0]*26

for i in n:
    arr[ord(i)-ord('a')]+=1

for i in arr:
    print(i,end=" ")

# 비효율적이기는 한데 볼 점이 있다.
# str = input()
 
# result = [0] * 26
 
# for i in range(str):
#     result[ord(i) - 97] = str.count(i)// str.count(i)는 i라는 문자가 str에 몇개 있는지 출력해준다. 
    
# for i in result:
#     print(i, end=" ")