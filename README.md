# 금융 마이데이터 RAG 활용 LLM 어플리케이션

인턴 업무중 금융 마이데이터 업무에 활용하기 위해서 금융정보원 마이데이터 가이드.pdf를 챗봇에 적용시킨 LLM 어플리케이션입니다.

1. Upstage chat, embedding API를 활용하였습니다. 
2. Pinecone Vector DB를 사용하였습니다. 
3. Retrieval 효율 개선을 위한 데이터 전처리, 키워드 Dictionary를 구축하였으며.
4. FewShot 예시를 첨부하여 답변 성능을 향상시켰습니다.
6. LangSmith를 활용하여 답변 성능을 평가하였습니다.
7. 완성된 모델을 Streamlit을 활용하여 챗봉형태의 웹 어플리케이션으로 구축하였습니다.
