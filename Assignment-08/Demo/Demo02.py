from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def calculator(expression):
    """
    This calculator function solve any arithmetic expression contain all
    contant values.It supports basic arthmetic operatiors +,-,*,/,and par
    Only answer the final value in short.

    :parm expression: str input arithmeic expression
    :returns expresion result as str
    """
    try:
        result=eval(expression)
        return str(result)
    except:
        return"error:Cannot solve expression"

llm=init_chat_model(
    model="phi-3-mini-4k-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not needed"
)

agent=create_agent(
    model=llm,
    tools=[
        calculator
    ],
    system_prompt="You are a helpful assistant. Answer in short."
)
while True:
    user_input=input("Me:")
    if user_input=="exit":
        break
    result=agent.invoke({
        "messages":[
            {"role":"user","content":user_input}
        ]    
    })
    llm_output=result["messages"][-1]
    print("AI:",llm_output.content)
    print("\n\n",result["messages"])