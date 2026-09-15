from dotenv import load_dotenv
from mem0 import MemoryClient

load_dotenv()

client = MemoryClient()

# messages = [
#     {
#         "role": "user",
#         "content": "Meu nome é Otavio e eu gosto de fazer automações com IA!",
#     },
#     {
#         "role": "assistant",
#         "content": "Oi Otavio! Anotei que você gosta de constuir automações com IA! Vou manter isso em mente para recomendações e discussões relacionadas.",
#     },
# ]

# client.add(messages, user_id="otavio")


client.add("Sou o Otavio e gosto de robótica!", user_id="otavio")

query = "Qual o meu nome?"
response = client.search(query, filters={"user_id": "otavio"})
response
response["results"][0]["memory"]
