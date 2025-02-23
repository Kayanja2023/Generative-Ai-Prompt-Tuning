"""
Python Script: Chatbot Prompting

This script demonstrates prompt engineering techniques to enhance chatbot interactions.

Topics Covered:
- Defining chatbot personality and tone
- Context retention for multi-turn conversations
- Handling user errors and ambiguous queries
"""

import openai

# Set up API Key
openai.api_key = "your-api-key"

def chat_with_ai(user_input, chat_history=[]):
    """Generates chatbot responses using OpenAI's GPT model while maintaining conversation context."""
    chat_history.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=chat_history
    )
    
    bot_response = response["choices"][0]["message"]["content"]
    chat_history.append({"role": "assistant", "content": bot_response})
    return bot_response, chat_history

# Example Chatbot Interaction
if __name__ == "__main__":
    print("AI Chatbot - Type 'exit' to end the conversation.")
    chat_history = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response, chat_history = chat_with_ai(user_input, chat_history)
        print("Chatbot:", response)