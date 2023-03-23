#Broadcasting

import numpy as np

# Cộng vector v với mỗi hàng của ma trận x, kết quả lưu ở ma trận y.

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # Tạo 1 array có chiều giống x

for i in range(4):
    y[i, :] = x[i, :] + v

print(y)


# Cộng kiểu broadcasting trong python
print(x + v)

# => Same result