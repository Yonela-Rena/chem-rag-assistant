import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(context, question):
    prompt =f"""
You are an expert Organic Chemistry tutor.

Answer ONLY using the information provided in the context.

Write your answer in simple English suitable for a university student.

If possible:
- Define the concept.
- Explain why it is important.
- Mention related reactions or examples.
- Keep the answer between 100 and 200 words.

If the answer cannot be found in the context, reply:

"I could not find that information in the provided chemistry notes."

Context:
{context}

Question:
{question}

Answer:
"""
    response = model.generate_content(prompt)

    return response.text