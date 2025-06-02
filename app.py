import streamlit as st

st.title("筋トレ記録アプリ")

exercise = st.text_input("種目を入力", "")
weight = st.number_input("重量 (kg)", min_value=0)
reps = st.number_input("回数", min_value=0)

if st.button("記録する"):
    st.success(f"{exercise} {weight}kg × {reps}回 を記録しました！")
