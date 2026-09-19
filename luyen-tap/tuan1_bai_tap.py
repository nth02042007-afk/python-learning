# ==================================================
#  BAI TAP LUYEN TAP - TUAN 1
#  Kien thuc duoc phep dung: bien, input/print, phep toan, if/else, f-string
#
#  Cach lam: viet code cua ban vao ben duoi moi de bai.
#  Chay thu:  python tuan1_bai_tap.py
# ==================================================


# --------------------------------------------------
# BAI 1: Dien tich & chu vi hinh chu nhat
#   - Cho chieu dai va chieu rong (tu gan bien).
#   - Tinh va in ra dien tich va chu vi.
#   - Ket qua mong doi voi dai=8, rong=5:  Dien tich = 40, Chu vi = 26
# --------------------------------------------------

# (viet code Bai 1 o day)
dai = 8
rong=5
dientich = dai*rong
chuvi = (dai + rong )*2
print(f"dientich: {dientich}")
print(f"chuvi:{chuvi}")
# --------------------------------------------------
# BAI 2: Doi nhiet do C sang F
#   - Cho nhiet do do C (tu gan bien).
#   - Cong thuc: F = C * 9/5 + 32
#   - In ra ket qua.
#   - Ket qua mong doi voi 37 do C:  98.6 do F
# --------------------------------------------------

# (viet code Bai 2 o day)

C = 8
F= C*9/5 +32
print(f"do c la :{C} do F la {F}")
# --------------------------------------------------
# BAI 3: Kiem tra so chan hay le
#   - Gan bien so (vi du so = 7).
#   - In ra so do la CHAN hay LE.
#   - Goi y: dung  so % 2 == 0  trong if/else.
#   - Ket qua mong doi voi so = 7:  so 7 la so LE
# --------------------------------------------------

# (viet code Bai 3 o day)
a = float(input( " nhập a:"))

if a%2==0:
    print(" a là số chẵn")
else:
    print ( " a là số lẻ ")
# --------------------------------------------------
# BAI 4: Diem trung binh & xep loai
#   - Cho diem 3 mon: toan, van, anh (tu gan bien).
#   - Tinh diem trung binh dtb = (toan + van + anh) / 3.
#   - Xep loai theo dtb:
#       dtb >= 8.0         -> "Gioi"
#       6.5 <= dtb < 8.0   -> "Kha"
#       5.0 <= dtb < 6.5   -> "Trung binh"
#       con lai            -> "Yeu"
#   - Goi y: dung if / elif / else.
#   - Ket qua mong doi voi toan=9, van=7, anh=8:  dtb = 8.0 -> Gioi
# --------------------------------------------------

# (viet code Bai 4 o day)
Toan = float(input("nhập điểm toán:" ))
Van = float(input("nhập điểm văn :"))
Anh = float(input("nhập điểm anh :"))
DTB = ( Toan + Van + Anh)/ 3
if DTB >=8:
    print (" Giỏi")
elif DTB >=6.5 :
    print (" Khá")
elif DTB >=5:
    print ("Trung Bình")
else :
    print (" yếu ")

# --------------------------------------------------
# BAI 5: Tinh tien dien bac thang
#   - Nhap so dien tieu thu so_kwh tu ban phim (dung input + float).
#   - Gia bac 1: 2000 VND / kWh cho 100 kWh dau.
#   - Gia bac 2: 3000 VND / kWh cho phan vuot qua 100 kWh.
#   - In ra so tien phai tra.
#   - Vi du 150 kWh -> 100*2000 + 50*3000 = 350000 VND
# --------------------------------------------------
# (viet code Bai 5 o day)
KLW = int(input(" Nhập số klw:"))
if KLW<=100:
    tiendien = KLW*2000
    print("Tiền điện tháng này :",tiendien)
else :
    tiendien = (KLW-100)*3000 +100*2000
print ( " tiền điện tháng này :",tiendien)

# --------------------------------------------------
# BAI 6: Tinh chi so BMI & phan loai
#   - Nhap can nang (kg) va chieu cao (met) tu ban phim (dung input + float).
#   - Cong thuc: BMI = can_nang / (chieu_cao * chieu_cao)
#   - In ra BMI (lam tron 1 chu so thap phan cung duoc) va phan loai:
#       BMI < 18.5           -> "Thieu can"
#       18.5 <= BMI < 25.0   -> "Binh thuong"
#       25.0 <= BMI < 30.0   -> "Thua can"
#       BMI >= 30.0          -> "Beo phi"
#   - Goi y: dung if / elif / else giong Bai 4.
#   - Vi du: nang=60 kg, cao=1.70 m  ->  BMI = 20.8  ->  Binh thuong
# --------------------------------------------------

# (viet code Bai 6 o day)
Chieu_cao= float(input("nhập chiều cao"))
Can_nang = float(input("Nhập cân nặng:"))
BMI = Can_nang/(Chieu_cao*Chieu_cao)
print(f" BMI là : {BMI}")
if BMI<18.5:
    print("gầy")
elif BMI >= 18.5 and BMI<25 :
    print(" bình thường")
elif BMI>=25.0 and BMI<30:
    print (" thừa cân")
else :
    print ( " béo phì")