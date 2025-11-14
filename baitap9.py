kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))
if kwh <= 100:
    total = kwh * 1678
elif kwh <= 200:
    total = 100 * 1678 + (kwh - 100) * 1734
elif kwh <= 300:
    total = 100 * 1678 + 100 * 1734 + (kwh - 200) * 2014
else:
    total = 100 * 1678 + 100 * 1734 + 100 * 2014 + (kwh - 300) * 2536 
    print(f"Tổng tiền điện phải trả: {total:.0f} VNĐ")