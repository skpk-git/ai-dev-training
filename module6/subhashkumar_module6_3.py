# subhashkumar_module6_3.py


# make UI using streamlit to interact with LLM to get user question and return the result store the result of the chat in SQL DB as text. 
# 


import sqlite3
import streamlit as st

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# Configuration
# --------------------------------------------------

DOCUMENT = "document.docx"
DATABASE = "chat_history.db"


# --------------------------------------------------
# Database functions
# --------------------------------------------------

def create_database():
    """Create the chat history table if it does not exist."""

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_chat(question, answer):
    """Save the question and answer to SQLite."""

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO chat_history (question, answer)
        VALUES (?, ?)
    """, (question, answer))

    connection.commit()
    connection.close()


# --------------------------------------------------
# Load document and create RAG
# --------------------------------------------------

@st.cache_resource
def create_rag():

    loader = Docx2txtLoader(DOCUMENT)

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    # Ollama embedding model
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Create vector database
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    # Retrieve top 3 chunks
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # Local Ollama LLM
    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    return retriever, llm


# --------------------------------------------------
# Ask LLM
# --------------------------------------------------

def ask_llm(question, retriever, llm):

    # Retrieve top 3 relevant document chunks
    retrieved_documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the question ONLY using the information
provided in the document context.

If the answer cannot be found in the context,
say:

"I could not find the answer in the document."

Do not make up information.

Document context:
{context}

Question:
{question}

Answer:
""")

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    return response.content


# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.set_page_config(
    page_title="RAG Chat",
    page_icon="🤖"
)

st.title("🤖 Document AI Assistant")

st.write(
    "Ask a question about the information contained "
    "in the document."
)


# Create database
create_database()


# Create RAG system
retriever, llm = create_rag()


# --------------------------------------------------
# Chat input
# --------------------------------------------------

question = st.chat_input("Ask a question...")


if question:

    # Display user's question
    with st.chat_message("user"):
        st.write(question)

    # Get answer from LLM
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_llm(
                question,
                retriever,
                llm
            )

        st.write(answer)


    # Save question and answer
    save_chat(
        question,
        answer
    )


    st.success("Chat saved to database.")


# --------------------------------------------------
# Show previous chat history
# --------------------------------------------------

st.sidebar.title("Chat History")

connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()

cursor.execute("""
    SELECT question, answer, created_at
    FROM chat_history
    ORDER BY id DESC
""")

history = cursor.fetchall()

connection.close()


for question, answer, created_at in history:

    with st.sidebar.expander(question):

        st.write(answer)

        st.caption(
            f"Created: {created_at}"
        )

#python -m pip install langchain langchain-community langchain-ollama langchain-chroma chromadb docx2txt
#ollama pull llama3.2
#ollama pull nomic-embed-text

#python -m streamlit run subhashkumar_module6_3.py