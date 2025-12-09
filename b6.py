def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def in_so_nguyen_to_trong_khoang(a, b):
    print(f"Các số nguyên tố trong khoảng từ {a} đến {b}:")
    for num in range(a, b + 1):
        if la_so_nguyen_to(num):
            print(num, end=" ")
    print()

in_so_nguyen_to_trong_khoang(1, 50)
