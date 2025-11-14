def main():
    RATE = 24500.0  # 1 USD = 24500 VND
    try:
        vnd = float(input("Nhập số tiền (VND): ").strip())
    except ValueError:
        print("Dữ liệu nhập không hợp lệ.")
        return

    usd = vnd / RATE
    print(f"{vnd:.2f} VND = {usd:.2f} USD (tỷ giá 1 USD = {RATE:.0f} VND)")

if __name__ == "__main__":
    main()