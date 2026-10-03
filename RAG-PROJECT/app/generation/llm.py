import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question: str, context: str):

    prompt = f"""
    You are an enterprise knowledge assistant.

    Answer the user's question using ONLY the provided sources.

    Rules:
    1. Do not use information that is not present in the sources.
    2. If the sources do not contain enough information, say:
    "I don't have enough information in the provided documents."
    3. Cite the source number when making a factual claim.
    4. Do not invent citations.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful enterprise knowledge assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content