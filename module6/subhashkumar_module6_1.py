# subhashkumar_module6_1.py

# .use langchain framework to imeplement a RAG to store a .doc file and then retrive 3 top choices  

# python -m pip install langchain langchain-community langchain-ollama langchain-chroma chromadb docx2txt

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# Configuration
# --------------------------------------------------

DOCUMENT = "document.docx"
VECTOR_DB = "./chroma_db"

LLM_MODEL = "llama3.2"
EMBEDDING_MODEL = "nomic-embed-text"


# --------------------------------------------------
# 1. Load DOCX document
# --------------------------------------------------

print("Loading document...")

loader = Docx2txtLoader(DOCUMENT)
documents = loader.load()

print(f"Loaded {len(documents)} document(s)")


# --------------------------------------------------
# 2. Split document into chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


# --------------------------------------------------
# 3. Create embeddings
# --------------------------------------------------

embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)


# --------------------------------------------------
# 4. Store in Chroma vector database
# --------------------------------------------------

vectorstore = Chroma(
    collection_name="my_documents",
    embedding_function=embeddings,
    persist_directory=VECTOR_DB
)

# Add document chunks
vectorstore.add_documents(chunks)

print("Document stored in vector database.")


# --------------------------------------------------
# 5. Create retriever
# --------------------------------------------------

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 3
    }
)


# --------------------------------------------------
# 6. Create Ollama LLM
# --------------------------------------------------

llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)


# --------------------------------------------------
# 7. Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful assistant.

Answer the user's question using ONLY the information
provided in the context.

If the answer is not available in the context,
say "I don't know based on the document."

Context:

{context}

Question:

{question}

Answer:
"""
)


# --------------------------------------------------
# 8. Ask questions
# --------------------------------------------------

while True:

    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() == "exit":
        break

    # Retrieve TOP 3 relevant chunks
    retrieved_docs = retriever.invoke(question)

    print("\n--- TOP 3 RETRIEVED CHUNKS ---")

    for i, doc in enumerate(retrieved_docs, start=1):

        print(f"\n### Result {i}")
        print(doc.page_content[:500])

    # Combine retrieved chunks
    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    # Create prompt
    messages = prompt.invoke({
        "context": context,
        "question": question
    })

    # Ask LLM
    response = llm.invoke(messages)

    print("\n--- ANSWER ---")
    print(response.content)
    