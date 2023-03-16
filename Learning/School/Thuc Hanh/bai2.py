from math import sqrt
import random


# bai 2.1
def snt(n):
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def printSnt():
    num = random.randint(0, 100)
    if snt(num):
        print(f'{num} là số nguyên tố.', end=' ')
    else:
        print(f'{num} không phải là số nguyên tố.', end=' ')


# bai 2.2
def soHoanHao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False


def printSoHoanHao():
    num = random.randint(0, 100)  # 6 28...
    if soHoanHao(num):
        print(f'{num} là số số hoàn hảo.', end=' ')
    else:
        print(f'{num} không phải là là số số hoàn hảo.', end=' ')


# bai 2.3
def deQuyTinhTong(n):
    if n == 0:
        return 0
    else:
        return n + deQuyTinhTong(n-1)


def printDeQuyTinhTong():
    n = random.randint(0, 100)
    print(f'S=1+2+3+...+{n} có kết quả là: {deQuyTinhTong(n)}')


# bai 2.4
def timSoLonNhat():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    max_value = max(a, b, c)
    print("Số lớn nhất là:", max_value)


# bai 2.5
def tongCacSntTrongKhoang1000():
    tong = 0
    count = 0

    for i in range(1001):
        if snt(i):
            # print('ds snt: ', i)
            count += 1
            tong += i

    # print('Số lượng snt: ', count)
    print('Tổng các số nguyên tố từ 0 đến 1000 là: ', tong)


# bai 2.6
def giaTriTuyetDoiCuaSoNguyen():
    n = int(input('Nhập 1 số nguyên bất kỳ: '))
    print('Giá trị tuyệt đối của số nguyên vừa nhập là: ', abs(n))


# bai 2.7
def tinhGiaiThua(n):
    if n == 0:
        return 1
    return n * tinhGiaiThua(n - 1)


def printTinhGiaiThua():
    number = random.randint(0, 8)
    print(f'Giai thừa của số nguyên dương {number} là {tinhGiaiThua(number)}')


# bai 2.8
def usclnCuaAvaB():
    a = int(input("Nhập số nguyên dương a = "))
    b = int(input("Nhập số nguyên dương b = "))

    temp1 = a
    temp2 = b
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2
        else:
            temp2 -= temp1
    uscln = temp1
    print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln)


# bai 2.10
def chuoiDoiXung(str):
    if str[::-1] == str:
        return True
    else:
        return False


def printChuoiDoiXung():
    str = input('Nhập vào 1 chuỗi: ')
    if (chuoiDoiXung(str)):
        print(f'{str} là 1 chuỗi đối xứng!')
    else:
        print(f'{str} không phải là 1 chuỗi đối xứng!')


# bai 2.9
# ...

# bai 2.11
def demSoTu():
    str = input('Nhập 1 chuỗi bất kỳ: ')
    _str = str.split()
    print(f'Tổng số từ trong chuỗi \'{str}\' là: {len(_str)}')


# bai 2.12
def handleNameOfSomeone():
    str = input('Nhập vào họ & tên đầy đủ: ')
    _str = str.split()
    print(f'Tên của người đó là: {_str[-1]}')


#  bai 2.13
def chuanHoaTen():
    str = input('Nhập vào họ & tên đầy đủ: ')
    print(f'Tên của người đó sau khi chuẩn hóa là: {str.title()}')


# bai 2.14
def noiChuoi():
    str1 = input('Nhập chuỗi thứ 1: ')
    str2 = input('Nhập chuỗi thứ 2: ')
    _str = ' '.join([str1, str2])
    _str = _str.replace(' ', '')
    print(f'Chuỗi sau khi nối có {len(_str)} ký tự')


# bai 2.15
def chuanHoaChuoi():
    str = input('Nhập 1 chuỗi bất kỳ: ')
    _str = ' '.join(str.split())
    print(f'Chuỗi sau chuẩn hóa là \'{_str}\'')


# bai 2.16
def sortString():
    str = input("Nhập chuỗi các từ: ").split()
    _str = sorted(set(str))
    __str = ' '.join(_str)

    print("Loại bỏ trùng lặp & sắp xếp: ", __str)


# bai 2.17
def demSoChuCaiVaSo():
    str = input("Nhập 1 câu: ")
    demSoChuCai = 0
    demSo = 0

    for _str in str:
        # kt nếu ký tự là chữ cái
        if (_str.isalpha()):
            demSoChuCai += 1
        # kt nếu ký tự là số
        elif (_str.isdigit()):
            demSo += 1

    print(
        f"Số ký tự là chữ cái trong câu là [{demSoChuCai}] & số ký tự là số trong câu là [{demSo}]")


########### Main ##########
# 2.1 Hàm & truyền tham số cho hàm
# printSnt()
# printSoHoanHao()
# printDeQuyTinhTong()
# timSoLonNhat()
# tongCacSntTrongKhoang1000()
# giaTriTuyetDoiCuaSoNguyen()
# printTinhGiaiThua()
# usclnCuaAvaB()


# 2.2 Chuỗi ký tự
# printChuoiDoiXung()
# demSoTu()
# handleNameOfSomeone()
# chuanHoaTen()
# noiChuoi()
# chuanHoaChuoi()
# sortString()
# demSoChuCaiVaSo()
