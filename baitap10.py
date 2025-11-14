salary_base = float(input("Nhập lương cơ bản (VNĐ): "))
work_days = int(input("Nhập số ngày công trong tháng: "))
daily_salary = salary_base / 22
salary = daily_salary * work_days
if work_days > 22:
    bonus = salary * 0.10   # Thưởng 10%
    salary += bonus
    print("Có thưởng 10% vì làm trên 22 ngày.")
elif work_days < 22:
    penalty = salary * 0.05  # Phạt 5%
    salary -= penalty
    print("Bị phạt 5% vì làm dưới 22 ngày.")
else:
    print("Không thưởng, không phạt (đủ 22 ngày).")
print(f"Lương thực nhận: {salary:.0f} VNĐ")
