import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

print(f"Checking API Key: {api_key[:10]}***" if api_key else "❌ API Key NOT found in .env!")

try:
    print("Connecting to Groq AI (Llama 3)...")
    
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )
    response = llm.invoke("پایتون چیست؟ به زبان فارسی و کوتاه پاسخ بده.")
    
    print("\n✅ SUCCESS!")
    print("AI Persian Response:", response.content)

except Exception as e:
    print("\n❌ FAILED!")
    print(f"Error Details: {e}")