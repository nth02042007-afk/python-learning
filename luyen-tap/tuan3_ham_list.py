# ==================================================
#  BAI TAP LUYEN TAP - TUAN 3
#  Chu de moi: HAM (def) & DANH SACH (list)
#  Kien thuc duoc phep dung: tat ca tuan 1-2 + def, return, list,
#                            .append(), len(), for ... in list
#
#  Cach lam: viet code cua ban vao ben duoi moi de bai.
#  Chay thu:  python tuan3_ham_list.py
# ==================================================


# --------------------------------------------------
# BAI 1: Ham chao hoi
#   - Viet ham chao(ten) nhan vao mot cai ten.
#   - Ham in ra:  Xin chao, <ten>!
#   - Sau do goi ham 2 lan voi 2 ten khac nhau.
#   - Goi y:
#       def chao(ten):
#           print(f"Xin chao, {ten}!")
#       chao("Hai")
# --------------------------------------------------

# (viet code Bai 1 o day)
def chao(ten):
    print(f"xin chao,{ten}")
chao(Hải)

# --------------------------------------------------
# BAI 2: Ham tinh tong 2 so (dung return)
#   - Viet ham tong(a, b) TRA VE (return) tong cua a va b.
#   - Goi ham, luu ket qua vao bien, roi in ra.
#   - Khac Bai 1: bai nay dung 'return' de tra ket qua, KHONG print trong ham.
#   - Goi y:
#       def tong(a, b):
#           return a + b
#       kq = tong(3, 5)
#       print(kq)          # 8
# --------------------------------------------------

# (viet code Bai 2 o day)


# --------------------------------------------------
# BAI 3: Ham kiem tra so chan/le
#   - Viet ham kiem_tra(so) tra ve chuoi "CHAN" hoac "LE".
#   - Goi y: dung if/else + return trong ham.
#   - Goi ham voi vai so va in ket qua.
#   - Vi du: kiem_tra(7) -> "LE"
# --------------------------------------------------

# (viet code Bai 3 o day)


# --------------------------------------------------
# BAI 4: Lam quen danh sach (list)
#   - Tao list diem = [8, 6, 9, 7, 10]
#   - In ra:
#       + So luong phan tu (dung len(diem))
#       + Phan tu dau tien (diem[0]) va cuoi cung (diem[-1])
#   - Dung vong lap for de in tung diem tren mot dong.
#   - Goi y:  for d in diem:
# --------------------------------------------------

# (viet code Bai 4 o day)


# --------------------------------------------------
# BAI 5: Tinh diem trung binh tu list
#   - Cho list diem = [8, 6, 9, 7, 10]
#   - Dung vong lap cong don tat ca diem lai, roi chia cho len(diem).
#   - In ra diem trung binh.
#   - Vi du list tren -> dtb = 8.0
#   - (Nang cao: thu dung ham co san sum(diem) / len(diem) de kiem tra)
# --------------------------------------------------

# (viet code Bai 5 o day)


# --------------------------------------------------
# BAI 6: Nhap N so vao list roi tim so lon nhat
#   - Nhap so luong N.
#   - Dung vong lap for + input de nhap N so, moi so .append() vao list.
#   - Tim so lon nhat trong list (tu viet vong lap, hoac dung max()).
#   - In ra list va so lon nhat.
#   - Goi y:
#       ds = []
#       ds.append(x)      # them x vao cuoi list
# --------------------------------------------------

# (viet code Bai 6 o day)
