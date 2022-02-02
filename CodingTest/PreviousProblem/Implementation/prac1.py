n = input()
left = sum(map(int, n[:len(n)//2]))
# print(left)
right = sum(map(int, n[len(n)//2:]))
# print(right)
if left == right:
    print("LUCKY")
else:
    print("READY")