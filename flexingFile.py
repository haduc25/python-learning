# import csv

class SanPham:
    def __init__(self, maSp, tenSp, gia):
        self.maSp = maSp
        self.tenSp = tenSp
        self.gia = gia

    def getMaSp(self):
        return self.maSp

    def setMaSp(self, maSp):
        self.maSp = maSp

    def getTenSp(self):
        return self.tenSp

    def setTenSp(self, tenSp):
        self.tenSp = tenSp

    def getGia(self):
        return self.gia

    def setGia(self, gia):
        self.gia = gia

class QuanLySanPham:
    def __init__(self):
        self.dssp = []
        self.next_id = 1

    def themSp(self, tenSp, gia):
        sp = SanPham(self.next_id, tenSp, gia)
        self.dssp.append(sp)
        self.next_id += 1

    def tkSpTheoId(self, maSp):
        for sp in self.dssp:
            if sp.maSp == maSp:
                return sp
        return None

    def tkSpTheoTuKhoa(self, keyword):
        rs = []
        for sp in self.dssp:
            if keyword.lower() in sp.tenSp.lower():
                rs.append(sp)
        return rs

    def xoaSp(self, maSp):
        for sp in self.dssp:
            if sp.maSp == maSp:
                self.dssp.remove(sp)
                break

    def suaSp(self, maSp, tenSpMoi, giaMoi):
        sp = self.tkSpTheoId(maSp)
        if sp is not None:
            sp.tenSp = tenSpMoi
            sp.gia = giaMoi

    def sxTheoId(self):
        self.dssp.sort(key=lambda sp: sp.maSp)

    def sxTheoTenSp(self):
        self.dssp.sort(key=lambda sp: sp.tenSp)

    def hienThiSp(self, sp):
        print('='*25, end = '\n')
        print(f"ID sản phẩm: {sp.maSp}")
        print(f"Tên sản phẩm: {sp.tenSp}")
        print(f"Giá: {sp.gia}")

    def hienThiDssp(self, dssp=None):
        if dssp is None:
            dssp = self.dssp
        for sp in dssp:
            self.hienThiSp(sp)

    def ghiFile(self, tenFile):
        if not self.dssp:
            print("Không có dữ liệu để ghi vào file!")
            return
        with open(tenFile, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Tên sản phẩm", "Giá"])
            for sp in self.dssp:
                writer.writerow([sp.maSp, sp.tenSp, sp.gia])
        print(f"Ghi dữ liệu vào file {tenFile} thành công!")


    def docFile(self, tenFile):
        with open(tenFile, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # bỏ qua header
            for row in reader:
                maSp, tenSp, gia = row
                self.themSp(tenSp, float(gia))

    def nhapDssp(self, n):
        for i in range(n):
            print(f"Nhập thông tin sp {i+1}:")
            tenSp = input("Tên sản phẩm: ")
            gia = float(input("Giá: "))
            self.themSp(tenSp, gia)

           
qlsp = QuanLySanPham()
n = int(input('Nhập số lượng sản phẩm: '))

qlsp.nhapDssp(n)
qlsp.hienThiDssp()


# Tìm kiếm sản phẩm trong danh sách theo Id
idSp = int(input('\nNhập ID sản phẩm muốn tìm kiếm: '))
rs = qlsp.tkSpTheoId(idSp)
if rs is None:
    print(f"Không tìm thấy sản phẩm có id là {idSp}")
else:
    qlsp.hienThiSp(rs)

# Tìm kiếm sản phẩm trong danh sách theo từ khóa
keywordSp = input('\nNhập từ khóa muốn tìm kiếm: ')
rs = qlsp.tkSpTheoTuKhoa(keywordSp)
if rs:
    print(f"Kết quả tìm kiếm cho từ khóa là {keywordSp}:")
    qlsp.hienThiDssp(rs)
else:
    print(f"Không tìm thấy sản phẩm có từ khóa là {keywordSp}")

# Xóa một sản phẩm khỏi danh sách
idSpDel = int(input('\nNhập ID sản phẩm muốn xóa: '))
qlsp.xoaSp(idSpDel)
print(f'\nDanh sách sản phẩm sau khi xóa ID {idSpDel}')
qlsp.hienThiDssp()

# Sửa thông tin sản phẩm theo Id
print('\nSửa thông tin sản phẩm theo Id\n')

idSp = int(input('Nhập ID sản phẩm cần được sửa: '))
rs = qlsp.tkSpTheoId(idSp)
if rs is None:
    print(f"Không tìm thấy sản phẩm có id là {idSp}")
else:
    newName = input('Tên sản phẩm: ')
    newPrice = float(input('Giá sản phẩm: '))
    qlsp.suaSp(idSp, newName, newPrice)
    print(f'\nCập nhật lại danh sách sản phẩm')
    qlsp.hienThiDssp()

# Sắp xếp danh sách theo Id tăng dần
qlsp.sxTheoId()
print(f'\nCập nhật lại danh sách sản phẩm sau khi sắp xếp theo Id')
qlsp.hienThiDssp()

# Sắp xếp danh sách theo tên sản phẩm tăng dần
qlsp.sxTheoTenSp()
print(f'\nCập nhật lại danh sách sản phẩm sau khi sắp xếp theo Tên sản phẩm')
qlsp.hienThiDssp()

# Ghi danh sách sản phẩm ra file
qlsp.ghiFile("btth4_files/sanpham.csv")

# Đọc danh sách sản phẩm từ file
qlsp.docFile("btth4_files/sanpham.csv")
qlsp.hienThiDssp()