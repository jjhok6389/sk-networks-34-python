import streamlit as st

st.title("사용자 입력 받는 페이지")

col1, col2= st.columns(2)

with col1:
    nickname = st.text_input("닉네임 입력하세요:")

    age = st.number_input("나이를 입력하세요:", min_value=13, max_value=100)

    national_list = ['한국', '중국', '일본', '미국', '외계']
    
    national = st.selectbox("국적", national_list)
    
    hobby_list =  ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질']
    
    hobby = st.radio('취미', hobby_list)
    
    is_checked = st.checkbox("개인정보 제공 동의")

    
with col2:
    if st.button('입력완료'):
        st.write(f"입력된 이름: {nickname}")
        st.write(f"입력된 나이는 {age}세 입니다.")
        st.write(f"선택된 국적: {national}")
        st.write(f"선택된 취미: {hobby}")
        st.write(f"개인정보 제공에 동의해?: {is_checked}")