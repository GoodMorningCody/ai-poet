# # .env 로드
# from dotenv import load_dotenv
# load_dotenv()

# 챗모드로 ChatGPT 연동
from langchain.chat_models import ChatOpenAI 
import streamlit as st
chat_model = ChatOpenAI()

# 타이틀
st.title("인공지능 시인")

# 주제 입력
content = st.text_input("시의 주제를 입력해주세요.", "")

# 시 작성 요청 및 OpenAI API 호출, 결과 표시
if st.button("시 작성 요청하기"):
    with st.spinner("시 작성 중..."):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)