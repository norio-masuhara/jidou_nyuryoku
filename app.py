import streamlit as st
st.title('履歴書　自動入力')
uploaded = st.file_uploader('data.txtをここにドロップ', type ='txt')
if uploaded:
    text = uploaded.read().decode('utf-8')
    st.text(text)
