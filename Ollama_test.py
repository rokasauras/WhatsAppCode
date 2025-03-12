import ollama
import sys
sys.stdout.reconfigure(encoding='utf-8')


desired_model = "deepseek-r1:8b"
question_to_ask = "Hello! How are you doing today?"


response = ollama.chat(
    model=desired_model,
    messages=[
        {
            "role": "user",
            "content": question_to_ask
        }
    ]
)


print(response)

if "message" in response and "content" in response["message"]:
    ollama_response = response["message"]["content"]
elif "content" in response:
    ollama_response = response["content"]
else:
    ollama_response = str(response)

print("Final Response:\n", ollama_response)

with open("OllamaResponse.txt", "w", encoding="utf-8") as f:
    f.write(ollama_response)
