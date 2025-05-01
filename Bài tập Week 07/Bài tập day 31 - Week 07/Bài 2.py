import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

w, b = 0.0, 0.0
learning_rate = 0.01
epochs = 1000

for _ in range(epochs):
    for i in range(len(X)):
        y_pred = w*X[i] + b
        loss = (y_pred - y[i])**2
        w = w - learning_rate*2*(y_pred - y[i])*X[i]
        b = b - learning_rate*2*(y_pred - y[i])

# Calculate predictions for all X values
y_pred = w * X + b

# Vẽ đồ thị
plt.scatter(X, y, label="Data")
plt.plot(X, y_pred, color='red', label="Regression Line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

print(f"Hệ số tối ưu: w = {w:.3f}, b = {b:.3f}")