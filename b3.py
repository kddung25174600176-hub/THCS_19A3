def kiem_tra_so_armstrong(n):
    chu_so = str(n)
    tong = sum(int(c)**3 for c in chu_so)
    return tong == n
print(kiem_tra_so_armstrong(157))
print(kiem_tra_so_armstrong(100))
print(kiem_tra_so_armstrong(153))

