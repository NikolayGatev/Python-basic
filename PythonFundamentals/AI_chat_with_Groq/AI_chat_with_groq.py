from groq import Groq
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API key do not add.")
# Initialize Groq API client
client = Groq(
    api_key=api_key,  # Replace with your own API key
)

# Function to get chat completion from Groq API
async def get_ai_response(user_input):
    try:
        chat_completion = await client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
async def main():
    print("AI Chat (type 'exit' or 'quit' to end the conversation)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        response = await get_ai_response(user_input)
        print("AI: " + response)

if __name__ == "__main__":
    asyncio.run(main())