
# biến
# title = "hello"

# hàm
# def getTitle

# hash table
object = {
    "id": 123,
    "name": "abc"
}

# class : lớp đối tượng
# thuộc tính:
# phương thức:

# đối tượng => lớp đối tượng

# lớp đối tượng Product
# thuộc tính: id, name, price
# phương thức: in ra thông tin Product, tính chiết khấu (price * 5)

# hàm tạo: gán giá trị khi khai báo đối tượng

# lớp đối tượng

# string template


class Product:

    def __init__(self, id, name, price):
        self.id = id  # 1
        self.name = name  # An
        self.price = price  # 10

    def infoProduct(self):
        print(f" id: {self.id} \n name: {self.name}  \n price: {self.price} ")

    def tinhChietKhau(self, phanTram):
        return self.price*phanTram

    # price + % chiet khau
    def tinhKhuyenMai(self):
        chietKhau = self.tinhChietKhau(10)
        return self.price + chietKhau


# đối tượng
product = Product(1, "An", 10)


class NhanVien:
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong):
        self.maNhanVien = maNhanVien
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.chucVu = chucVu
        self.heSoLuong = heSoLuong

    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong


class GiamDoc(NhanVien):
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong, tienThuong):
        super().__init__(maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong)
        self.tienThuong = tienThuong

    def luongCuoiCung(self):

        return self.tinhLuong() + self.tienThuong


class QuanLy(NhanVien):
    def __init__(self, maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong, truLuong):
        super().__init__(maNhanVien, tenNhanVien, luongCoBan, chucVu, heSoLuong)
        self.truLuong = truLuong

    def luongCuoiCung(self):
        return self.tinhLuong() - self.truLuong

# nhân viên
nhanVien = NhanVien(1, "An", 10, "NV", 0)
print(nhanVien.tinhLuong())

# giám đốc
giamDoc = GiamDoc(1, "Teo", 10, "GD", 1, 100)
print(giamDoc.luongCuoiCung())

# quản lý
quanLy = QuanLy(1, "Mam", 10, "QL", 10, 1000)
print(quanLy.luongCuoiCung())
