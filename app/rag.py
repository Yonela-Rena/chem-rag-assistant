from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.llm import ask_llm

# Load embedding model once
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database once
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


def ask_question(question: str):

    results = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    answer = ask_llm(context, question)

    return answer