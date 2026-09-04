from groq import Groq

client = Groq()

response = client.chat.completions.create(
    model="qwen/qwen3.6-27b",
    messages=[
        {"role": "system", "content": "Atue como um especialista em machine learning"},
        {"role": "user", "content": "De forma simples, o que é machine learning"},
    ],
    temperature=0,
    top_p=1,
)

print(response.choices[0].message.content)
