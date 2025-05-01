import streamlit as st
import openai
import os

openai.api_key = st.secrets["chatbot"]

st.title("Chat với GPT-4o")

# Sửa: loại bỏ khoảng trắng thừa trong key
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị các tin nhắn trước đó
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Khi người dùng nhập prompt
if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gửi yêu cầu đến GPT-4o
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages
    )

    # Trích xuất nội dung trả lời
    reply = response.choices[0].message.content

    # Hiển thị và lưu tin nhắn trả lời
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
