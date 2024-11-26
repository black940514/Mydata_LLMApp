import streamlit as st


from dotenv import load_dotenv


from llm import get_ai_response

st.set_page_config(page_title="김태연의 마이데이터 챗봇", page_icon="💰")

st.title("💰 김태연의 마이데이터 챗봇")
st.caption("마이데이터2.0 질문에 답변해드립니다.")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])




if user_question := st.chat_input(placeholder="마이데이터에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다"):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})
