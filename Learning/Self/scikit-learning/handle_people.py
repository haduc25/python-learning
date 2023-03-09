import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset into a pandas dataframe
data = pd.read_csv('Learning/Self/scikit-learning/people.csv', delimiter=';')

# Extract the Weight and Height columns as the features and target variable
X = data['weight'].values.reshape(-1, 1)   # Reshape to a 2D array
y = data['height'].values.reshape(-1, 1)

# Fit a linear regression model to the data
model = LinearRegression()
model.fit(X, y)

# Ask the user to input a weight value
weight = float(input("Enter weight (in kg): "))

# Predict the height of a person with the entered weight
predicted_height = model.predict([[weight]])
print('Predicted height:', predicted_height[0, 0])
