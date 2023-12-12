0. python3, pip 설치
1. platform.openapi.com 에서 api 발급
2. .env에 키 등록.
(langchain에서 variable 정의되어 있어 동일한 이름 사용)
```
OPENAI_API_KEY=키
```

3. dotenv 설치
```
$pip install python-dotenv
```

4. main.py 추가
```py
# .env 파일을 로드
from dotenv import load_dotenv
load_dotenv()
```

5. langchain 설치
```
$pip install langchain
```

6. openai 설치
```
$pip install openai
```

7. streamlit 배포를 위해 requirements.txt 파일 추가 후 작성
```
langchain
openai
```

8. 랭체인 hello world
```py
# .env에서 openai_api_key 로드
from dotenv import load_dotenv
load_dotenv()

# complete mode(legacy)
from langchain.llms import OpenAI
llm = OpenAI()
result = llm.predict("hi!")
print(result)

# chat mode(system, user, assist 분리)
from langchain.chat_models import ChatOpenAI 
chat_model = ChatOpenAI()
result = chat_model.predict("hi!")
print(result)
```

9. 프론트 엔지니어링을 위해 streamlit 설치
```
$pip install streamlit
```

10. streamlit을 import 시킨 후 필요한 엘리먼트 추가
```py
import streamlit as st

st.title("this is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
```

11. 터미널에서 streamlit run main.py 실행
```
$streamlit run main.py
```

12. requirements.txt에 streamlit 추가
```
langchain
openai
streamlit
```

13. streamlit으로 text_input, button, spinner, write 등을 사용해 프론트엔드 구성 및 api 연동
```py
# .env 로드
from dotenv import load_dotenv
load_dotenv()

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
```

13. 배포
```
깃헙에 .env 제거 후 업로드, streamlit에 가입 후 깃헙 선택, .env 에 작성한 값을 advanced settings에 "" 넣어서 추가 및 배포
```
