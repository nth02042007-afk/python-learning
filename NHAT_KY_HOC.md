# 📔 NHẬT KÝ HỌC PYTHON — NGUYEN HAI

> Ghi lại những gì đã học theo từng ngày. Đọc lại trước khi học bài mới.

---

## 🗓️ Ngày 15/09/2026 — Tuần 1: Biến & Câu điều kiện

### ✅ Đã học được
- **Biến & phép toán:** gán giá trị, `*`, `/`, `+`, `-`, dùng ngoặc `( )` để ưu tiên.
- **Nhập dữ liệu:** `input()` luôn trả về **chuỗi (text)** → phải bọc `float(...)` hoặc `int(...)` để tính toán.
  ```python
  diem = float(input("Nhập điểm: "))
  n    = int(input("Nhập số: "))
  ```
- **f-string** để in đẹp: `print(f"Diện tích: {dientich}")`.
  - Làm tròn số thập phân: `{bmi:.1f}` → in `20.8` thay vì `20.7612...`.
- **Câu điều kiện `if / elif / else`:** kiểm tra mốc từ cao xuống thấp (hoặc thấp lên cao) cho nhất quán.
  ```python
  if dtb >= 8:      xep = "Giỏi"
  elif dtb >= 6.5:  xep = "Khá"
  elif dtb >= 5:    xep = "Trung bình"
  else:             xep = "Yếu"
  ```
- **Chẵn/lẻ:** dùng `so % 2 == 0`.

### 🐛 Lỗi mình hay mắc (NHỚ KỸ!)
| Lỗi | Sai | Đúng |
|---|---|---|
| Gõ nhầm tên hàm | `intput(...)` | `input(...)` — Python gợi ý *"Did you mean: 'input'?"* |
| Ngoặc nhọn sai | `print(x, {tien})` → in `{350000}` | `print(x, tien)` → in `350000` |
| Thụt lề (indent) sai | Lệnh nằm ngoài `if/else` → **luôn chạy**, in trùng | Chỉ thụt lề đúng khối cần chạy |
| Điều kiện elif thừa | `elif BMI <= 18.5 and BMI < 25` (không bao giờ đúng) | `elif BMI < 25` (vì `>= 18.5` đã chắc chắn) |

### 📝 Bài đã làm
- File: `luyen-tap/tuan1_bai_tap.py` — 6 bài: hình chữ nhật, đổi C→F, chẵn/lẻ, xếp loại điểm, tiền điện bậc thang, BMI.
- Kết quả kiểm chứng: điểm 9-7-8 → **Giỏi**; 150 kWh → **350000đ**; cao 1.70m nặng 60kg → **Bình thường**.

### ➡️ Học tiếp theo
- File: `luyen-tap/tuan2_vong_lap.py` — **Vòng lặp `for` / `while` + `range()`**.
  - Nhớ: `range(1, 11)` = 1 → **10** (số cuối KHÔNG lấy).
  - `while` + `break` để dừng vòng lặp.

---

## 🗓️ Ngày 20/09/2026 — Tuần 2: Vòng lặp (for / while)

### ✅ Đã học được
- **`for` + `range()`:** lặp số lần biết trước.
  ```python
  for i in range(1, 11):   # i = 1,2,...,10
      print(i)
  ```
  - ⭐ Quy tắc vàng: muốn chạy tới **N** thì viết `range(1, N + 1)` (số cuối KHÔNG lấy).
- **Cộng dồn:** `tong = 0` trước vòng lặp → `tong = tong + i` trong vòng lặp → in **ngoài** vòng lặp.
- **Đếm có điều kiện:** `for` + `if` + biến đếm `dem = dem + 1` (chỉ +1 khi thỏa điều kiện).
- **`while`:** lặp đến khi điều kiện sai. Nhớ đọc input mới **BÊN TRONG** vòng lặp.
  ```python
  dap_an = 7
  doan = int(input("Đoán: "))
  while doan != dap_an:
      print("Sai rồi")
      doan = int(input("Đoán: "))   # phải thụt lề trong while!
  print("Chính xác!")
  ```
- **Nhân dồn (giai thừa):** `gt = 1` (KHÔNG phải 0) → `gt = gt * i`.

### 🐛 Lỗi mình hay mắc (NHỚ KỸ!)
| Lỗi | Sai | Đúng |
|---|---|---|
| Quên +1 ở range | `range(1, N)` (thiếu số cuối) | `range(1, N + 1)` |
| Cộng/nhân dồn khởi tạo sai | nhân dồn để `= 0` → luôn ra 0 | nhân dồn `= 1`, cộng dồn `= 0` |
| Gán đè thay vì đếm | `dem = i + 1` | `dem = dem + 1` |
| `print` trong vòng lặp | in trùng nhiều lần | kéo ra ngoài, in 1 lần |
| **while lặp vô tận** | đọc input NGOÀI while → treo máy | thụt lề lệnh đọc input VÀO TRONG while |
| f-string | `(dem)` in ra chữ | `{dem}` mới in giá trị |

### 📝 Bài đã làm
- File: `luyen-tap/tuan2_vong_lap.py` — 6 bài: in 1→10, tính tổng, bảng cửu chương, đếm số chẵn, đoán số (while), giai thừa. Tất cả chạy đúng ✅.

### ➡️ Học tiếp theo
- Tuần 3: **Hàm (`def`)** và **danh sách (`list`)**.

---

<!-- Ngày học mới thêm mục ## ở bên dưới -->
