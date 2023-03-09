import pandas as pd
import time
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset into a pandas dataframe
data = pd.read_csv('Learning/Self/scikit-learning/people2.csv', delimiter=';')


# Extract the Weight and Height columns as the features and target variable
X = data['nang'].values.reshape(-1, 1)  # Reshape to a 2D array
y = data['cao'].values.reshape(-1, 1)

# Fit a linear regression model to the data
model = LinearRegression()
model.fit(X, y)

# Prompt user for weight input
weight = float(input('Nhập cân nặng (kg): '))

# Add a loading text while calculating the predicted height
print('Đang tính toán chiều cao dự đoán...')
for i in range(5):
    print('.' * i, end='\r')
    time.sleep(0.5)

# Predict the height based on the user input weight
predicted_height = model.predict([[weight]])

# Display the predicted height
print(
    f"Chiều cao dự đoán với cân nặng {weight} kg: {predicted_height[0, 0]:.2f} cm")

# Plot the regression line
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Cân nặng (kg)')
plt.ylabel('Chiều cao (cm)')
plt.title('Hồi quy chiều cao vs. cân nặng')
plt.show()
