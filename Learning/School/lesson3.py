import time
import datetime
import os

start = time.perf_counter()

time.sleep(1)

end = time.perf_counter()

print(f'end: {end}, start: {start} and result is: {end - start}')
print(end - start)  # 👉️ 1.0010583459988993

print(datetime.datetime.now())


######################################################################
os.system('cls')

# Giải quyết bài toán


def giaiThua(n):
    if n == 0 or n == 1:
        return 1
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt


rs = giaiThua(123)
print(rs)
