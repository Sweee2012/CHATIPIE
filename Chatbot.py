import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Direct API key (secure this in real apps)
api_key = "AIzaSyBkbhM-E2aNUVeN76ygVeK9Ebfyx2jWRcM"

# Gemini response function
def get_gemini_response(input_text):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    message = [HumanMessage(content=input_text)]
    response = llm.invoke(message)
    return response.content

# Streamlit UI
st.set_page_config(page_title="🤖 Chatipie", page_icon="💬")
st.title("💬 Chatipie - Ask Anything!")

st.markdown("Ask me a question and get a smart answer using **Gemini 2.0 Flash**.")

input = st.text_input("Enter your question:", key="input")

if st.button("Generate"):
    if input:
        response = get_gemini_response(input)
        st.subheader("🧠 Chatipie's Response:")
        st.write(response)
    else:
        st.warning("Please enter a question before clicking")
