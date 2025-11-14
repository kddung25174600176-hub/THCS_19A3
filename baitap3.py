def main():
    try:
        base = float(input("Nhập độ dài cạnh đáy (đơn vị): ").strip())
        height = float(input("Nhập chiều cao (đơn vị): ").strip())
    except ValueError:
        print("Dữ liệu nhập không hợp lệ.")
        return

    area = 0.5 * base * height
    print(f"Diện tích tam giác: {area:.2f}")

if __name__ == "__main__":
    main()
    