import numpy as np
import matplotlib.pyplot as plt

# Tối ưu hóa hàm f(x) = x^4 - 3x^2 + 2
def f(x):
    return x**4 - 3*x**3 + 2

def  f_prime(x):
    return 4*x**3 - 9*x**2

# Gradient descent
def gradient_descent(f_prime, x_init, learning_rate=0.01, epochs=100):
    x = x_init
    history = [x]

    for _ in range(epochs):
        x = x - learning_rate * f_prime(x)
        history.append(x)

    return x, history

 # Chạy Gradient Descent
x_init = 0.5
learning_rate = 0.01
epochs = 100
x_optimal, history = gradient_descent(f_prime, x_init, learning_rate, epochs)

# Vẽ đồ thị
x_vals = np.linspace(-1, 3, 100)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(history, [f(x) for x in history], color="red", s=10, label="Iterations")
plt.scatter(x_optimal, f(x_optimal), color="green", marker="x", s=100, label=f"Min at x={x_optimal:.3f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()