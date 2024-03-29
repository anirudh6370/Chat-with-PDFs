import streamlit as st
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
from pdf_utils import get_pdf_text
from vectorstore_utils import get_text_chunks, get_vectorstore
from conversation_utils import get_conversation_chain
# from dotenv import load_dotenv
# import os
# load_dotenv()

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    apikey = st.text_input(label="Enter your OpenAI API Key",type="password")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        try:
            if st.button("Process") :
                with st.spinner("Processing"):
                    # get pdf text
                    raw_text = get_pdf_text(pdf_docs)

                    # get the text chunks
                    text_chunks = get_text_chunks(raw_text)

                    # create vector store
                    vectorstore = get_vectorstore(text_chunks,apikey)

                    # create conversation chain
                    st.session_state.conversation = get_conversation_chain(
                        vectorstore,apikey)
        except Exception as e:
            st.write("Enter the open ai api key")

if __name__ == '__main__':
    main()
