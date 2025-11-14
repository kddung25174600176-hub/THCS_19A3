def main():
    try:
        principal = float(input("Nhập số tiền gửi ban đầu (VND): ").strip())
        annual_rate_percent = float(input("Nhập lãi suất hàng năm (%): ").strip())
    except ValueError:
        print("Dữ liệu nhập không hợp lệ.")
        return

    r = annual_rate_percent / 100.0
    interest_1_month = principal * r * (1/12)
    interest_2_quarters = principal * r * (6/12)  # 2 quý = 6 tháng
    interest_3_years = principal * r * 3  # 3 năm

    print(f"Lãi sau 1 tháng (lãi đơn): {interest_1_month:.2f} VND")
    print(f"Lãi sau 2 quý (6 tháng, lãi đơn): {interest_2_quarters:.2f} VND")
    print(f"Lãi sau 3 năm (lãi đơn): {interest_3_years:.2f} VND")

if __name__ == "__main__":
    main()