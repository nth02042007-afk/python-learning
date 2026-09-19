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

<!-- Ngày học mới thêm mục ## ở bên dưới -->
