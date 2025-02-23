"""
Python Script: AI Prompt Tuning

This script demonstrates various prompt tuning techniques to refine AI responses for better accuracy and relevance.

Topics Covered:
- Basic text generation with OpenAI's GPT
- Optimizing prompts with structured input
- Experimenting with different prompt variations
- Enhancing response quality using context-aware tuning
"""

import openai

# Set up API Key
openai.api_key = "your-api-key"

def generate_text(prompt):
    """Generates AI-powered text based on a given prompt."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Example 1: Basic Prompt
basic_prompt = "Explain the importance of responsible AI."
basic_response = generate_text(basic_prompt)

# Example 2: Context-Aware Prompt
context_prompt = "As a data scientist, explain the importance of responsible AI in ensuring fairness and reducing bias."
context_response = generate_text(context_prompt)

# Example 3: Step-by-Step Explanation
step_prompt = "Describe the process of training a machine learning model in five detailed steps."
step_response = generate_text(step_prompt)

print("Basic Response:", basic_response)
print("Context-Aware Response:", context_response)
print("Step-by-Step Response:", step_response)
