import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.4
)

print("🤖 AI Medical Chatbot Ready (OpenAI). Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Take care! 👋")
        break

    response = llm.invoke([
        HumanMessage(
            content=f"""
You are an AI medical assistant.
User symptoms: {user_input}python -m pip install langchain langchain-core langchain-openai openai

Suggest common medicines, home remedies,
and basic precautions.
Clearly advise consulting a doctor if symptoms are serious.
Do not provide prescription dosages.
"""
        )
    ])

    print("Bot:", response.content)
