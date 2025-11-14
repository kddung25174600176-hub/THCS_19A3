def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

def main():
    try:
        year = int(input("Nhập một năm (ví dụ 2024): ").strip())
    except ValueError:
        print("Dữ liệu nhập không hợp lệ.")
        return

    if is_leap_year(year):
        print(f"{year} là năm nhuận.")
    else:
        print(f"{year} không phải là năm nhuận.")

if __name__ == "__main__":
    main()