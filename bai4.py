import math

n = int(input("Nhập n: "))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(f"Các số nguyên tố nhỏ hơn {n}:")
for i in range(2, n):
    if is_prime(i):
        print(i, end=" ")
