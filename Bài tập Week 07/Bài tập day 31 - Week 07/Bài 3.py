# Tìm cực tiểu của hàm số f(x) = x^3 - 6x^2 + 4x + 12
# f'(x) = 3x^2 - 12x + 4
# f''(x) = 6x - 12

def f(x):
    return x**3 - 6*x**2 + 4*x + 12

def f_prime(x):
    return 3*x**2 - 12*x + 4

def f_double_prime(x):
    return 6*x - 12

x = 5
for _ in range(10):
    x = x - f_prime(x) / f_double_prime(x)

print(f"Cực tiểu tại x = {x:.3f}")
