def main():
    username = input("Nhập tên đăng nhập: ").strip()
    password = input("Nhập mật khẩu: ").strip()

    # Theo đề: kiểm tra nếu username là "admin" và mật khẩu không phải "password123"
    if username == "admin" and password != "password123":
        print("Quyền truy cập: ĐƯỢC PHÉP")
    else:
        print("Quyền truy cập: BỊ TỪ CHỐI")

if __name__ == "__main__":
    main()