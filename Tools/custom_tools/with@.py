from langchain_core.tools import tool

# create a function,add type hints and then add tool decorator to create a func
@tool
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b
#tool decorator helps llm communicate

result=multiply.invoke({"a":40,"b":10})
print(result)
#sepical attrubutes
print(multiply.name)
print(multiply.description)
print(multiply.args)