# ==================================================
#  BAI TAP LUYEN TAP - TUAN 2
#  Chu de moi: VONG LAP (for / while) + range()
#  Kien thuc duoc phep dung: bien, input/print, phep toan,
#                            if/else, f-string, for, while, range()
#
#  Cach lam: viet code cua ban vao ben duoi moi de bai.
#  Chay thu:  python tuan2_vong_lap.py
# ==================================================


# --------------------------------------------------
# BAI 1: In cac so tu 1 den 10
#   - Dung vong lap for + range().
#   - In moi so tren mot dong.
#   - Goi y: for i in range(1, 11):
# --------------------------------------------------

# (viet code Bai 1 o day)

for i in range(1, 11):
 print (i)
#
# --------------------------------------------------
# BAI 2: Tinh tong tu 1 den N
#   - Nhap N tu ban phim (dung input + int).
#   - Dung vong lap cong don: tong = tong + i.
#   - In ra tong.
#   - Vi du N = 100  ->  tong = 5050
# --------------------------------------------------

# (viet code Bai 2 o day)
tong =0
n = int(input(" nhập N:"))
for i in range ( 1,n+1):
  tong = tong + i
print ( tong)
# --------------------------------------------------
# BAI 3: In bang cuu chuong
#   - Nhap so n (vi du n = 7).
#   - In ra bang cuu chuong cua n tu 1 den 10.
#   - Ket qua mong doi voi n = 7:
#       7 x 1 = 7
#       7 x 2 = 14
#       ...
#       7 x 10 = 70
# --------------------------------------------------

# (viet code Bai 3 o day)

n= int(input(" Nhập N:"))
for i in range (1,11):
  print(f"{n}X{i}= {n*i}")

# --------------------------------------------------
# BAI 4: Dem so chan trong khoang 1..N
#   - Nhap N tu ban phim.
#   - Dung for + if de dem xem co bao nhieu so chan tu 1 den N.
#   - In ra so luong so chan.
#   - Vi du N = 10  ->  co 5 so chan (2,4,6,8,10)
# --------------------------------------------------

# (viet code Bai 4 o day)
n = int(input("Nhập N:"))
for i in range(1,n+1):
  if i %2==0:
    print(i)
    

# --------------------------------------------------
# BAI 5: Doan so (dung while)
#   - Cho san dap an bi mat, vi du:  dap_an = 7
#   - Dung vong lap while: lien tuc yeu cau nguoi choi nhap so
#     cho den khi doan dung thi dung lai.
#   - Neu doan sai thi in "Sai roi, thu lai".
#   - Neu doan dung thi in "Chinh xac!" va thoat vong lap (break).
# --------------------------------------------------

# (viet code Bai 5 o day)


# --------------------------------------------------
# BAI 6 (NANG CAO): Tinh giai thua N!
#   - Nhap N tu ban phim.
#   - Giai thua N! = 1 * 2 * 3 * ... * N.
#   - Dung vong lap nhan don: gt = gt * i (bat dau gt = 1).
#   - In ra ket qua.
#   - Vi du N = 5  ->  5! = 120
# --------------------------------------------------

# (viet code Bai 6 o day)
