# subhashkumar_module6_2.py

#integrate python code (module 5 . Q.7)  with RAG. Let the LLM answer question from my .docs by retrieving top 3 answers   

from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# 1. Load the document
# --------------------------------------------------

DOCUMENT = "document.docx"

loader = Docx2txtLoader(DOCUMENT)
documents = loader.load()


# --------------------------------------------------
# 2. Split document into smaller chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Document loaded.")
print(f"Number of chunks: {len(chunks)}")


# --------------------------------------------------
# 3. Create embeddings using Ollama
# --------------------------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# --------------------------------------------------
# 4. Store chunks in Chroma
# --------------------------------------------------

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)


# --------------------------------------------------
# 5. Create retriever
#    k=3 means retrieve TOP 3 chunks
# --------------------------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# --------------------------------------------------
# 6. Create local LLM
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 7. Prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the user's question ONLY using the information
provided in the retrieved document sections.

If the answer cannot be found in the retrieved sections,
say:

"I could not find the answer in the document."

Do not make up information.

Retrieved document sections:

{context}

Question:
{question}

Answer:
""")


# --------------------------------------------------
# 8. Ask questions
# --------------------------------------------------

while True:

    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    # Retrieve TOP 3 relevant chunks
    retrieved_docs = retriever.invoke(question)

    print("\n--- TOP 3 RETRIEVED SECTIONS ---")

    for i, doc in enumerate(retrieved_docs, start=1):
        print(f"\n--- Result {i} ---")
        print(doc.page_content)


    # Combine retrieved chunks
    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )


    # Create prompt
    messages = prompt.format_messages(
        context=context,
        question=question
    )


    # Ask LLM
    response = llm.invoke(messages)


    print("\n--- LLM ANSWER ---")
    print(response.content)    