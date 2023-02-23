import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import time

# đọc dữ liệu từ file csv
df = pd.read_csv('Learning/Self/scikit-learning/people2.csv',
                 delimiter=';', index_col=0)
print(df)

# vẽ biểu đồ minh họa dataset
plt.plot(df.cao, df.nang, 'ro')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.show()

# sử dụng hồi quy tuyến tính
X = df.loc[:, ['cao']].values   # X là dữ liệu đầu vào
y = df.nang.values              # y là dữ liệu đầu ra
model = LinearRegression()      # loại mô hình
model.fit(X, y)                 # tập huấn luyện trên dữ liệu


# vẽ lại sơ đồ
plt.scatter(X, y, c='b')
plt.plot(X, model.predict(X))
plt.show()

# dự báo 1 số tình huống
x = float(input('Nhập chiều cao: '))

for i in range(5):
    print('.' * i, end='\r')
    time.sleep(0.5)

print('Người cao', x, 'cm, dự đoán cân nặng ~', model.predict([[x]]))
