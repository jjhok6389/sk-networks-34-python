import streamlit as st

st.title("오늘은 수요일")
st.header("오늘은 Streamlit 배우는 날​")
st.subheader("Streamlit으로 나만의 데모 페이지 만들기~~~! ")

site = st.text_input("오늘 내가 만들고 싶은 사이트는??")

st.write(f"내가 만들고 싶은 사이트는:{site}")

if st.button(f"{site} 접속하기"):
    st.success(f"{site} 접속 중!!!!!")