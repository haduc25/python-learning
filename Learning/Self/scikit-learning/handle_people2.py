# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# # Load the dataset into a pandas dataframe
# data = pd.read_csv('Learning/Self/scikit-learning/people.csv', delimiter=';')

# # Extract the Weight and Height columns as the features and target variable
# X = data['weight'].values.reshape(-1, 1)   # Reshape to a 2D array
# y = data['height'].values.reshape(-1, 1)

# # Fit a linear regression model to the data
# model = LinearRegression()
# model.fit(X, y)

# # Ask the user to input a weight value
# weight = float(input("Enter weight (in kg): "))

# # Predict the height of a person with the entered weight
# predicted_height = model.predict([[weight]])
# print('Predicted height:', predicted_height[0, 0])

# # Plot the data points and the regression line
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.xlabel('Weight (kg)')
# plt.ylabel('Height (cm)')
# plt.title('Height vs Weight')
# plt.show()

import pandas as pd
import time
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset into a pandas dataframe
data = pd.read_csv('Learning/Self/scikit-learning/people.csv', delimiter=';')


# Extract the Weight and Height columns as the features and target variable
X = data['weight'].values.reshape(-1, 1)   # Reshape to a 2D array
y = data['height'].values.reshape(-1, 1)

# Fit a linear regression model to the data
model = LinearRegression()
model.fit(X, y)

# Prompt user for weight input
weight = float(input('Enter weight (in kg): '))

# Add a loading text while calculating the predicted height
print('Calculating...')
for i in range(5):
    print('.' * i, end='\r')
    time.sleep(0.5)

# Predict the height based on the user input weight
predicted_height = model.predict([[weight]])

# Display the predicted height
print(
    f"Predicted height for weight {weight} kg: {predicted_height[0, 0]:.2f} cm")

# Plot the regression line
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Height vs. Weight Regression')
plt.show()
