N,B = input().split()

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = N[::-1]
B = int(B)

sum= 0
for i in range(len(N)):
    sum +=system.index(N[i])*pow(B,i)

print(sum)