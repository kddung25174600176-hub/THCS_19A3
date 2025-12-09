def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_100_500():
    print("Các số nguyên tố từ 100 đến 500:")
    for num in range(100, 501):
        if la_so_nguyen_to(num):
            print(num, end=" ")
    print()

n=37
print(la_so_nguyen_to(n))    

in_so_nguyen_to_100_500()