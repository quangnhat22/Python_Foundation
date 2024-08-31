class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = khoaHoc

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)
        
    def hienThiKhoaHoc(self):
        for kh in self.khoaHoc:
            kh.hienThiThongTinKhoaHoc()

class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc 
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi  

    def hienThiThongTinKhoaHoc(self):
        print(f"------|Ma khoa hoc: {self.maKhoaHoc} - Ten khoa hoc: {self.tenKhoaHoc} - Hinh thuc: {self.hinhThuc} - Hoc phi: {self.hocPhi}")

def themHocVien():
    tenHV = input("Nhap ten hoc vien: ")
    ngaySinh = input("Nhap ngay sinh: ")
    hv = HocVien(f"HV{len(dsHocVien) + 1}", tenHV, ngaySinh, [])
    dsHocVien.append(hv)

    print("Them hoc vien thanh cong! Danh sach hoc vien sau khi them: ")
    hienThiHocVien()

def hienThiHocVien():
    for hv in dsHocVien:
        print(f"Ma hoc vien: {hv.maHV} - Ten hoc vien: {hv.tenHV} - Ngay sinh: {hv.ngaySinh} - Khoa hoc: ")
        hv.hienThiKhoaHoc()

def timHocVienTheoMa(maHV):
    for hv in dsHocVien:
        if hv.maHV == maHV:
            return hv
    return None

def dangKyKhoaHoc():
    hienThiHocVien()
    maHV = input("Nhap ma hoc vien: ")
    hv = timHocVienTheoMa(maHV)
    if hv is None:
        print("Khong tim thay hoc vien")
        return

    hienThiKhoaHoc()
    maKhoaHoc = input("Nhap ma khoa hoc: ")
    kh = timKhoaHocTheoMa(maKhoaHoc)
    if kh is None:
        print("Khong tim thay khoa hoc")
        return

    hv.dangKyKhoaHoc(kh)

    print("-------- Dang ky khoa hoc thanh cong! Danh sach hoc vien sau khi dang ky --------")
    hienThiHocVien()

def hienThiKhoaHoc():
    for kh in dsKhoaHoc:
        kh.hienThiThongTinKhoaHoc()

def themKhoaHoc():
    tenKhoaHoc = input("Nhap ten khoa hoc: ")
    hinhThuc = input("Nhap hinh thuc: ")
    hocPhi = int(input("Nhap hoc phi: "))
    kh = KhoaHoc(f"KH{len(dsKhoaHoc) + 1}", tenKhoaHoc, hinhThuc, hocPhi)
    dsKhoaHoc.append(kh)

def timKhoaHocTheoMa(maKhoaHoc):
    for kh in dsKhoaHoc:
        if kh.maKhoaHoc == maKhoaHoc:
            return kh
    return None

def hienThiThongTinKhoaHoc():
    maKhoaHoc = input("Nhap ma khoa hoc: ")
    kh = timKhoaHocTheoMa(maKhoaHoc)
    if kh is None:
        print("Khong tim thay khoa hoc")
        return
    kh.hienThiThongTinKhoaHoc()

def main():
     global dsHocVien
     global dsKhoaHoc
     dsHocVien = []
     dsKhoaHoc = []

     sv1 = HocVien("HV1", "Nguyen Van A", "01/01/2001", [])
     sv2 = HocVien("HV2", "Nguyen Van B", "02/02/2002", [])
    
     kh1 = KhoaHoc("KH1", "Lap trinh Python", "Offline", 1000)
     kh2 = KhoaHoc("KH2", "Lap trinh Java", "Online", 2000)

     dsHocVien.append(sv1)
     dsHocVien.append(sv2)

     dsKhoaHoc.append(kh1)
     dsKhoaHoc.append(kh2)

     while True:
        print("\n Nhap yeu cau: ")
        print("1. Them hoc vien: ")
        print("2. Dang ky khoa hoc: ")
        print("3. Hien thi khoa hoc: ")
        print("4. Them khoa hoc: ")
        print("5. Thong tin khoa hoc")
        print("6. Exit")

        try:
            choice = int(input("Nhap yeu cau: "))
            if choice == 1:
                themHocVien()
            elif choice == 2:
               dangKyKhoaHoc()
            elif choice == 3:
                hienThiKhoaHoc()
            elif choice == 4:
             themKhoaHoc()
            elif choice == 5:
                hienThiThongTinKhoaHoc()
            elif choice == 6:
                print("Thoat...")
                break
            else:
                print("Lua chon khong hop le!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

