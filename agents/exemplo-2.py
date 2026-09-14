import json

import yfinance as yf
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(base_url="https://api.groq.com/openai/v1")


def get_stock(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    output = {
        "ticker": ticker,
        "company_name": info.get("shortName", ticker),
        "current_price": info.get("currentPrice", 0),
    }
    return json.dumps(output)


tools = [
    {
        "type": "function",
        "name": "get_stock",
        "description": "Retorna informações básicas de uma ação.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Símbolo da ação. (ex: AAPL, NVDA)",
                },
            },
            "required": ["ticker"],
        },
    },
]

input_list = [{"role": "user", "content": "Qual o preço da ação da Apple?"}]

response = client.responses.create(
    model="openai/gpt-oss-20b",
    tools=tools,
    input=input_list,
)

# response.model_dump()

for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        result = get_stock(**args)
        input_list.append(item.model_dump())
        input_list.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result,
            }
        )

print("Final input:")
print(input_list)

final_response = client.responses.create(
    model="openai/gpt-oss-20b",
    instructions="Responda com uma análise baseada nos dados retornados pela função.",
    tools=tools,
    input=input_list,
)

print("Final output:")
print(final_response.model_dump_json(indent=2))
print("\n" + final_response.output_text)
