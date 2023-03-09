"""
    một ví dụ về việc sử dụng TensorFlow và Keras để xây dựng một mô hình mạng nơ-ron đơn giản 
    để phân loại hình ảnh:
    """
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Preprocess data
x_train = x_train.reshape(-1, 28 * 28).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28 * 28).astype("float32") / 255.0

# Define model
model = keras.Sequential(
    [
        layers.Dense(256, activation="relu"),
        layers.Dense(128, activation="relu"),
        layers.Dense(10),
    ]
)

# Compile model
model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss=keras.losses.SparseCategoricalCrossentropy(
    from_logits=True),
    metrics=["accuracy"])

# Train model
history = model.fit(x_train, y_train, batch_size=64,
                    epochs=10, verbose=2, validation_split=0.2)

# Evaluate model
test_scores = model.evaluate(x_test, y_test, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])
