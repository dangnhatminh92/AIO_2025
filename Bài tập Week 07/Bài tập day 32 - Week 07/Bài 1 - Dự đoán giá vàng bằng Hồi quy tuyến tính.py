import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dữ liệu mẫu
data = pd.read_csv('O:\AIO\AIO 2025\WARM UP - CODING and ALGORTHIMS\Week 7\Day 32\samples.csv')

X = data[['USD Index', 'Inflation', 'Oil Price']]
Y = data['Gold Price'].values.reshape(-1, 1)

X = np.array(X)
Y = np.array(Y)



class LinearRegression:
    def __init__(self):
        # Khởi tạo weights và bias bằng 0
        self.w = np.zeros((X.shape[1],1))# weights cho 3 features
        self.b = 0 # bias

    def gradient(self, X, Y, learning_rate):
        y_pred = self.predict(X)
        m = X.shape[0]
        dw = (1/m) * np.dot(X.T, (y_pred - Y))
        db = (1/m) * np.sum(y_pred - Y)
        return dw, db
    
    def predict(self, X):
        return np.dot(X, self.w) + self.b
    
    def fit(self, X, Y, learning_rate=0.001, epochs=10):
        for epoch in range(epochs):
            # Tính gradient và cập nhật weights, bias
            dw, db = self.gradient(X, Y, learning_rate)
            self.w = self.w - learning_rate * dw
            self.b = self.b - learning_rate * db

            loss =  np.mean((Y - self.predict(X))**2) / 2

            print(f'Epoch {epoch}, Loss: {loss:.2f}')

# Normalize chỉ features X để tránh overflow
X_normalized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Khởi tạo và huấn luyện mô hình
model = LinearRegression()
model.fit(X_normalized, Y, learning_rate=0.05, epochs=1000)

# In ra weights và bias cuối cùng
print("\nFinal weights:", model.w)
print("Final bias:", model.b)

# Dự đoán và so sánh kết quả
y_pred = model.predict(X_normalized)

print("\nSo sánh kết quả thực tế và dự đoán:")
for i in range(5):
    print(f"Thực tế: {Y[i][0]:.2f}, Dự đoán: {y_pred[i][0]:.2f}")
            

    


