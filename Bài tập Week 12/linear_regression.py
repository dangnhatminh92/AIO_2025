import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dữ liệu
df = pd.read_csv("/home/dangnhatminh92/Documents/AIO/AIO_2025/WARMING UP/Coding/Bài tập Week 12/advertising.csv")

X = df[["TV", "Radio", "Newspaper"]].values
y = df["Sales"].to_numpy().reshape(-1, 1)

# Chuẩn hóa dữ liệu đầu vào
X = (X - np.mean(X, axis=0)) / X.std(axis=0)
X_train = np.hstack([X, np.ones((len(X), 1))])


# Hàm huấn luyện Linear Regression

def train_linear_regression(X_train, y, lr=0.01, epochs=100, show_plot=False):
    theta = np.zeros((X_train.shape[1], 1))
    loss_history = []
    n_samples = len(X_train)

    if show_plot:
        plot_placeholder = st.empty()  # tạo vùng trống cho biểu đồ

    for epoch in range(epochs):
        y_pred = np.dot(X_train, theta)
        loss = np.mean((y_pred - y) ** 2)
        loss_history.append(loss)
        dtheta = (2 / n_samples) * (X_train.T @ (y_pred - y))
        theta = theta - lr * dtheta

        if show_plot and epoch % 10 == 0:  # mỗi 10 vòng update 1 lần cho mượt
            fig, ax = plt.subplots()
            ax.plot(loss_history)
            ax.set_xlabel("Epoch")
            ax.set_ylabel("MSE Loss")
            ax.set_title(f"Loss tại epoch {epoch}")
            plot_placeholder.pyplot(fig)
    return theta, loss_history

theta, loss_history = train_linear_regression(X_train, y)



# Giao diện Streamlit
st.title("Huấn luyện Linear Regression với Numpy")

lr = st.slider("Learning rate", 0.001, 0.1, 0.01)
epochs = st.slider("Số epoch", 10, 10000, 200)

if st.button("Train model"):
    theta, loss_history = train_linear_regression(X_train, y, lr, epochs, show_plot=True)
    theta = theta.flatten()

    st.write(f"Trọng số cuối cùng (w) và (b):", theta)
    st.write(f"Phương trình đường thẳng có dạng: $y = {theta[0]:.2f}x1 + {theta[1]:.2f}x2 + {theta[2]:.2f}x3 + {theta[3]:.2f}$")