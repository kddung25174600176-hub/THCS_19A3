def main():
    try:
        candies = int(input("Nhập tổng số kẹo: ").strip())
        students = int(input("Nhập số học sinh: ").strip())
    except ValueError:
        print("Dữ liệu nhập không hợp lệ.")
        return

    if students <= 0:
        print("Số học sinh phải lớn hơn 0.")
        return

    per_student = candies // students
    remainder = candies % students

    print(f"Mỗi học sinh nhận được: {per_student} kẹo")
    print(f"Số kẹo còn thừa: {remainder} kẹo")

if __name__ == "__main__":
    main()