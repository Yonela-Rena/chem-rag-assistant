from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from llm import ask_llm

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# Ask a question
query = input("Ask a chemistry question: ")

# Search for relevant chunks
results = vectorstore.similarity_search(query, k=3)

# Combine retrieved text into one context
context = "\n\n".join([doc.page_content for doc in results])

# Ask Gemini using the retrieved context
answer = ask_llm(context, query)

print("\n==============================")
print("Chemistry AI Answer")
print("==============================\n")
print(answer)