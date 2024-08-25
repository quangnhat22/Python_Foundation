class NhanVien:
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong):
        self.maNhanVien = maNhanVien
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.chucVu = chucVu
        self.heSoLuong = heSoLuong

    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong

    def hienThiThongTin(self):
        return f"""
            ID: {self.maNhanVien}
            Ten: {self.tenNhanVien}
            Luong co ban: {self.luongCoBan}
            Chuc vu: {self.chucVu}
            He so luong: {self.heSoLuong}"""

class QuanLy(NhanVien):
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, heSoLuong, tienThuong ,danhSachPhongBan):
        super().__init__(maNhanVien, tenNhanVien, luongCoBan, "Quan Ly", heSoLuong)
        self.tienThuong = tienThuong
        self.danhSachPhongBan = danhSachPhongBan

    def tinhLuong(self):
        return super().tinhLuong() + self.tienThuong

    def hienThiThongTin(self):
        return f"""
            ID: {self.maNhanVien}
            Ten: {self.tenNhanVien}
            Luong co ban: {self.luongCoBan}
            Chuc vu: {self.chucVu}
            He so luong: {self.heSoLuong}
            Tien thuong: {self.tienThuong}
            Phong ban quan ly: {', '.join(self.danhSachPhongBan)}"""

class GiamDoc(NhanVien):
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, heSoLuong, tienThuong, danhSachChiNhanh):
        super().__init__(maNhanVien, tenNhanVien, luongCoBan, "Giam Doc", heSoLuong)
        self.tienThuong = tienThuong
        self.danhSachChiNhanh = danhSachChiNhanh

    def tinhLuong(self):
        return super().tinhLuong() + self.tienThuong

    def hienThiThongTin(self):
        return f"""
            ID: {self.maNhanVien}
            Ten: {self.tenNhanVien}
            Luong co ban: {self.luongCoBan}
            Chuc vu: {self.chucVu}
            He so luong: {self.heSoLuong}
            Tien thuong: {self.tienThuong}
            Chi nhanh quan ly: {', '.join(self.danhSachChiNhanh)}"""



def main():
    nv1 = NhanVien("NV001", "Nguyen Van A", 1000, "Developer", 1.5)
    print(nv1.hienThiThongTin())
    print(nv1.tinhLuong())

    ql1 = QuanLy("QL001", "Nguyen Van B", 1000, 1.5, 2000, ["Phong Ban A", "Phong Ban B"])
    print(ql1.hienThiThongTin())
    print(ql1.tinhLuong())

    gd1 = GiamDoc("QL001", "Nguyen Van B", 1000, 1.5, 2000, ["Chi nhanh A", "Chi nhanh B"])
    print(gd1.hienThiThongTin())
    print(gd1.tinhLuong())

if __name__ == "__main__":
    main()