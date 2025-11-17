#tính S1
n = int(input())
S1 = n*(n+1)//2
print("S1 =", S1)
#tính S2
n = int(input())
S2 = 1
for i in range(1, n):
    S2 *= i
print("S2 =", S2)
#tính S3
n = int(input())
S3 = sum(((-1)**i)/i for i in range(1, n+1))
print("S3 =", S3)
#tính S4
n = int(input())
S4 = sum(k/(k+2) for k in range(n+1))
print("S4 =", S4)
