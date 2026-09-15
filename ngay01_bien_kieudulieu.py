# =========================================================
# NGÀY 1 — Biến & Kiểu dữ liệu cơ bản trong Python
# Chạy file này bằng lệnh:  python ngay01_bien_kieudulieu.py
# =========================================================

# 1) BIẾN: cái hộp chứa dữ liệu
ten = "An"          # chuỗi (str)
tuoi = 20           # số nguyên (int)
chieu_cao = 1.70    # số thực (float)
dang_di_hoc = True  # đúng/sai (bool)

# 2) IN RA MÀN HÌNH
print("Tên:", ten)
print("Tuổi:", tuoi)
print("Chiều cao:", chieu_cao, "m")
print("Đang đi học?", dang_di_hoc)

# 3) KIỂM TRA KIỂU DỮ LIỆU
print("Kiểu của ten :", type(ten))
print("Kiểu của tuoi:", type(tuoi))

# 4) f-string: ghép biến vào câu (cách hiện đại, nên dùng)
print(f"Xin chào, tôi là {ten}, {tuoi} tuổi.")

# 5) PHÉP TOÁN cơ bản
a = 10
b = 3
print("Tổng      :", a + b)   # 13
print("Hiệu      :", a - b)   # 7
print("Tích      :", a * b)   # 30
print("Thương    :", a / b)   # 3.333...
print("Chia lấy nguyên:", a // b)  # 3
print("Chia lấy dư    :", a % b)   # 1
print("Lũy thừa  :", a ** b)  # 1000

# 6) NHẬP LIỆU TỪ BÀN PHÍM (bỏ dấu # để thử)
# ten_nguoi_dung = input("Nhập tên của bạn: ")
# print(f"Chào {ten_nguoi_dung}!")
