import math

n = int(input("Nhập số n: "))

if int(math.sqrt(n))**2 == n:
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải số chính phương")
