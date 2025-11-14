def main():
    try:
        price = float(input("Nhập giá sản phẩm (VND): ").strip())
        qty = int(input("Nhập số lượng mua: ").strip())
    except ValueError:
        print("Giá hoặc số lượng không hợp lệ.")
        return

    subtotal = price * qty
    vat = subtotal * 0.10  # 10%
    total = subtotal + vat

    print(f"Tổng tiền trước VAT: {subtotal:.2f} VND")
    print(f"VAT (10%): {vat:.2f} VND")
    print(f"Tổng tiền phải trả: {total:.2f} VND")

if __name__ == "__main__":
    main()