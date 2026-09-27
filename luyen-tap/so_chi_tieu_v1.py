# ==================================================
#  SO CHI TIEU v1 - NGAY 12 (Tuan 3)
#  Chu de moi: HAM NHAN LIST, LIST RONG, THAM SO MAC DINH
#  Kien thuc duoc phep dung: tat ca tuan 1-3 + None, return som,
#                            tham so mac dinh (nguong=100000), round()
#
#  LUAT (B3): 4 ham duoi day CHI return - KHONG input(), KHONG print().
#  Chi tiet bai hoc: docs-python/week-03/day-12.md
#
#  Cach lam: viet code cua ban vao ben duoi moi de bai.
#  Chay thu:  python so_chi_tieu_v1.py
# ==================================================


# --------------------------------------------------
# BAI 1: Ham tong_chi(ds)
#   - Nhan vao list so tien, TRA VE tong so tien.
#   - Tu cong don bang vong lap (KHONG dung sum()).
#   - List rong [] -> tra ve 0.
#   - Goi y:
#       def tong_chi(ds):
#           tong = 0
#           for so_tien in ds:
#               ...
#           return tong      # chu y thut le: return NGOAI vong for
# --------------------------------------------------

# (viet code Bai 1 o day)
def tong_chi(ds):
        tong = 0
        for so_tien in ds:
            tong = tong+so_tien
        return tong  

# --------------------------------------------------
# BAI 2: Ham chi_lon_nhat(ds)
#   - TRA VE so tien lon nhat (tu viet vong lap, KHONG dung max()).
#   - List rong [] -> tra ve None (khong co khoan nao thi khong co "lon nhat").
#   - Goi y: kiem list rong o DAU ham roi return som:
#       if len(ds) == 0:
#           return None
#       lon_nhat = ds[0]
# --------------------------------------------------

# (viet code Bai 2 o day)


# --------------------------------------------------
# BAI 3: Ham trung_binh(ds)
#   - TRA VE round(tong / so khoan) -> so nguyen (tien la int - B1).
#   - GOI LAI ham tong_chi(ds), khong cong don lai lan nua.
#   - List rong [] -> tra ve 0 (tranh chia cho 0).
# --------------------------------------------------

# (viet code Bai 3 o day)


# --------------------------------------------------
# BAI 4: Ham dem_khoan_lon(ds, nguong=100000)
#   - TRA VE so khoan co so tien >= nguong.
#   - nguong co gia tri mac dinh 100000.
#   - List rong [] -> tra ve 0.
#   - Vi du: dem_khoan_lon(ds)          -> dung nguong 100000
#            dem_khoan_lon(ds, 120000)  -> dung nguong 120000
# --------------------------------------------------

# (viet code Bai 4 o day)


# --------------------------------------------------
# PHAN CHAY THU (viet sau khi xong 4 bai - ngay 14 se thay bang menu)
#   - Tao list: chi_tieu = [35000, 120000, 15000, 250000]
#   - In ket qua 4 ham, goi dem_khoan_lon 2 lan (mac dinh va 120000).
#   - In ket qua 4 ham voi list rong [] tren MOT dong.
#
#   Ket qua DUNG phai la:
#       Tong chi: 420000
#       Lon nhat: 250000
#       Trung binh: 105000
#       So khoan >= 100000: 2
#       So khoan >= 120000: 2
#       List rong: 0, None, 0, 0
# --------------------------------------------------

# (viet code phan chay thu o day)
