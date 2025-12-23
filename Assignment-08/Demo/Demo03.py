from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

@tool
def calculator(expression: str):
    """
    Solve arithmetic expressions.
    Supports +, -, *, /, (), numbers only.
    """
    allowed_chars = "0123456789+-*/(). "
    if not all(c in allowed_chars for c in expression):
        return "Error: Invalid characters in expression"

    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Cannot solve expression"


@tool
def get_weather(city):
    """
    Get current weather of a city.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Error: OPENWEATHER_API_KEY missing"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return "Error: City not found or API issue"

    data = response.json()

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }

    return json.dumps(weather_data)


@tool
def read_file(filepath: str):
    """
    Read text file content.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Error: File not found or unreadable"

SYSTEM_PROMPT = """
You are an AI assistant with access to tools.

Rules:
- If the user asks for math, you MUST use the calculator tool.
- If the user asks about weather of a city, you MUST use the get_weather tool.
- If the user asks to read a file, you MUST use the read_file tool.
- Do NOT answer from memory when tools are available.
- After using a tool, explain the result briefly.

Available tools:
calculator(expression)
get_weather(city)
read_file(filepath)
"""


llm = init_chat_model(
    model="phi-3-mini-4k-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed"
)


agent = create_agent(
    model=llm,
    tools=[calculator, get_weather, read_file],
    system_prompt=SYSTEM_PROMPT
)



print("AI Agent Ready (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    result = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    ai_message = result["messages"][-1].content
    print("AI:", ai_message)
