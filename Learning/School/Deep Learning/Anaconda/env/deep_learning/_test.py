# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:09:30 2023

@author: Admin
"""

# from keras.models import Sequential
# from keras.layers import Dense

# # Xác định kiến trúc mạng nơ-ron
# model = Sequential()
# model.add(Dense(10, input_dim=4, activation='relu'))
# model.add(Dense(3, activation='softmax'))

# # Biên dịch mô hình với hàm mất mát và thuật toán tối ưu hóa
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Huấn luyện mô hình với dữ liệu đào tạo
# model.fit(X_train, y_train, epochs=100, batch_size=10)

# # Đánh giá mô hình trên dữ liệu kiểm định
# loss, accuracy = model.evaluate(X_test, y_test)
# print("Độ chính xác trên dữ liệu kiểm định:", accuracy)

from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense

# Chuẩn bị dữ liệu
X = [[0, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Chia dữ liệu thành tập đào tạo và tập kiểm định
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Chuyển đổi nhãn thành dạng one-hot encoding
y_train = to_categorical(y_train, num_classes=2)
y_test = to_categorical(y_test, num_classes=2)

# Xác định kiến trúc mạng nơ-ron
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Biên dịch mô hình với hàm mất mát và thuật toán tối ưu hóa
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Huấn luyện mô hình với dữ liệu đào tạo
model.fit(X_train, y_train, epochs=100, batch_size=10)

# Đánh giá mô hình trên dữ liệu kiểm định
loss, accuracy = model.evaluate(X_test, y_test)
print("Độ chính xác trên dữ liệu kiểm định:", accuracy)

