from operator import truediv
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit.components.v1 as components
import pygwalker as pyg
import io

st.title("🚀 Phân tích dữ liệu từ file CSV")

uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(io.StringIO(uploaded_file.getvalue().decode("utf-8")))
    st.subheader("Dữ liệu ban đầu")
    st.dataframe(df.head())
    st.write("Số dòng:", df.shape[0])
    st.write("Số cột:", df.shape[1])

    st.subheader("Thông tin mô tả dữ liệu")
    st.write("Các thống kê cơ bản:")
    st.dataframe(df.describe())
    st.write("Kiểu dữ liệu:")
    st.write(df.dtypes)
    st.write("Số giá trị thiếu:")
    st.write(df.isnull().sum())


    option = st.selectbox("Chọn cột để phân tích", df.columns)
    if option:
        st.subheader(f"Phân tích dữ liệu cột: {option}")
        st.write(df[option].describe())
        st.write(df[option].value_counts())
        st.write(df[option].isnull().sum())


        st.subheader("Biểu đồ phân tích")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[option], ax=ax)
        st.pyplot(fig)
        
    option_corr = st.multiselect("Chọn cột để phân tích", df.columns)

    if option_corr:
        st.subheader(f"Hệ số tương quan giữa các cột: {option_corr}")
        corr_matrix = df[option_corr].corr()
        st.write(corr_matrix)
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        st.subheader("Tải file với cột đã chọn")
        st.download_button(
            label="📥 Tải xuống file CSV",
            data=df[option_corr].to_csv(index=False),
            file_name="du_lieu.csv",
            mime="text/csv"
        )

    st.divider()
    with st.expander("🔍 Phân tích dữ liệu tương tác với PygWalker", expanded=True):
        if st.button("⚙️ Tải PygWalker"):
            pyg_html = pyg.walk(df, return_html=True)
            if pyg_html:
                components.html(str(pyg_html), height=1000, scrolling=True)
