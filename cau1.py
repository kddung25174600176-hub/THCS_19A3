s = input("Nhập chuỗi: ")

chu_cai = chu_so = ky_tu_dac_biet = 0

for c in s:
    if c.isalpha():
        chu_cai += 1
    elif c.isdigit():
        chu_so += 1
    else:
        ky_tu_dac_biet += 1

print("Chữ cái:", chu_cai)
print("Chữ số:", chu_so)
print("Ký tự đặc biệt:", ky_tu_dac_biet)
