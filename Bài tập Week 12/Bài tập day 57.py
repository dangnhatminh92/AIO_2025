import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


############################
st.title("Ứng dụng vẽ đồ thị hàm số")
st.header("Bài 1: Vẽ đồ thị hàm số cơ bản")
option = st.selectbox(
    "Chọn hàm số cần vẽ:",
    ["Hàm sin", "Hàm cos", "Hàm log", "Hàm exp"]
)
st.write(f"Bạn đã chọn vẽ đồ thị của hàm: {option}")

if option == "Hàm sin":
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    st.line_chart(y)
elif option == "Hàm cos":
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.cos(x)
    st.line_chart(y)
elif option == "Hàm log":
    x = np.linspace(0, 10, 1000)
    y = np.log(x)
    st.line_chart(y)
elif option == "Hàm exp":
    x = np.linspace(0, 10, 1000)
    y = np.exp(x)
    st.line_chart(y)

st.divider()

st.header("Bài 2: So sánh 2 hàm số trên cùng một biểu đồ")
dict_function = {
    "Hàm sin": np.sin,
    "Hàm cos": np.cos,
    "Hàm log": np.log,
    "Hàm exp": np.exp
}
option = st.multiselect(
    "Chọn hàm số cần vẽ:",
    list(dict_function.keys())
)

for func in option:
    x = np.linspace(1e-10, 2 * np.pi, 1000)
    y = dict_function[func](x)
    st.line_chart(y)

st.divider()

st.header("Bài 3: Vẽ đồ thị hàm bậc 2")
a = st.number_input("Nhập hệ số a:")
b = st.number_input("Nhập hệ số b:")
c = st.number_input("Nhập hệ số c:")
st.markdown(f"Hàm bậc 2: $y = {a}x^2 + {b}x + {c}$")

x = np.linspace(-10, 10, 100)
y = a*x**2 + b*x + c
st.line_chart(y)

st.divider()

st.header("Bài 4: Tương tác với Slider để khảo sát đồ thị")
a = st.slider("Nhập hệ số a:", min_value=-10, max_value=10, value=1,step=1)
b = st.slider("Nhập hệ số b:", min_value=-10, max_value=10, value=1,step=1)
c = st.slider("Nhập hệ số c:", min_value=-10, max_value=10, value=1,step=1)
st.markdown(f"Hàm bậc 2: $y = {a}x^2 + {b}x + {c}$")

x = np.linspace(-10, 10, 100)
y = a*x**2 + b*x + c
st.line_chart(y)

st.divider()

st.header("Bài 5: Vẽ Heatmap cho hàm $z = x^2 + y^2$")

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig, ax = plt.subplots()
sns.heatmap(Z, cmap="viridis", ax=ax)
st.pyplot(fig)





