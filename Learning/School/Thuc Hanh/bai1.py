from math import sqrt

# bai 1.1


def soChanHoacSoLe(x):
    if (x % 2 == 0):
        print(f'{x} là số chẵn')
    else:
        print(f'{x} là số lẻ')


# bai 1.2
def soAmHoacSoDuong(x):
    if (x >= 0):
        print(f'{x} là số dương')
    else:
        print(f'{x} là số âm')

#
def tinhPtBacNhat():
    # ax + b = 0
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))

    if a == 0:
        if b == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print("Phương trình có nghiệm x =", -b / a)


# main
x = float(input('Nhập 1 số bất kỳ: '))
# soChanHoacSoLe(x)
# soAmHoacSoDuong(x)


###
def laNamNhuan(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# year = int(input('Nhập số năm: '))
# if laNamNhuan(year):
#     print(year, "là năm nhuận")
# else:
#     print(year, "không phải là năm nhuận")


#
def canbac2():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x = ", x)
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 = ", x1)
        print("x2 = ", x2)


# canbac2()


def isTamgiac():
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Khong tao thanh tam giac.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Khong tao thanh tam giac.")
    else:
        print("Tao thanh tam giac.")


# isTamgiac()


def isMax():
    a = float(input("Nhap so a: "))
    b = float(input("Nhap so b: "))

    # if (a > b):
    #     print(f'A={a} lớn hơn B={b}')
    # elif (a == b):
    #     print(f'A={a} bằng B={b}')
    # else:
    #     print(f'B={b} lớn hơn A={a}')


# isMax()

# # 1.10
# a = float(input("Nhap a: "))
# b = float(input("Nhap b: "))
# c = float(input("Nhap c: "))

# max_value = max(a, b, c)

# print("Gia tri lon nhat la:", max_value)


################################
def meow():
    # Nhập ngày, tháng, năm từ bàn phím
    day = int(input("Nhap ngay: "))
    month = int(input("Nhap thang: "))
    year = int(input("Nhap nam: "))

    # Kiểm tra năm nhuận
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        is_leap_year = True
    else:
        is_leap_year = False

    # Kiểm tra ngày, tháng, năm hợp lệ
    if year > 0 and 1 <= month <= 12:
        if month == 2:
            if is_leap_year:
                max_day = 29
            else:
                max_day = 28
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        if 1 <= day <= max_day:
            print("Ngay, thang, nam hop le.")
        else:
            print("Ngay khong hop le.")
    else:
        print("Nam khong hop le.")


# meow()


########################################
def snt(n):
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def printSnt():
    for i in range(1, 101):
        if snt(i):
            print(i, end=' ')


# printSnt()


def nhapSoNguyenDuong():
    tong = 0
    x = int(input('so nguyen duong: '))
    for i in range(1, x + 1):
        print(i)
        tong += i
    return tong


# print(nhapSoNguyenDuong())


def tongPtMang():
    tong = 0
    arr = [1, 5, 0, 5, 6]
    for i in range(len(arr)):
        print(arr[i])
        tong += arr[i]
    return tong


# print(tongPtMang())

# 1.15
def demSoChan():
    arr = [57, 39, 90, 14, 7, 44, 85, 54, 63, 23]
    dem = 0
    for i in arr:
        if (i % 2) == 0:
            dem += 1
    return dem


# print(demSoChan())


def maxTrongArr():
    arr = [25, 69, 18, 60, 58, 41, 75, 97, 81, 64]
    # print(max(arr))

    max_value = arr[0]
    for i in arr:
        if (i > max_value):
            max_value = i
    return max_value


# print(maxTrongArr())


def minTrongArr():
    arr = [25, 69, 18, 60, 58, 41, 75, 97, 81, 64]
    # print(min(arr))

    min_value = arr[0]
    for i in arr:
        if (i < min_value):
            min_value = i
    return min_value


# print(minTrongArr())
