#toolkit is a collection of related tools that serve a common purpose packaged together for convinence and resusability

#eg:GoogleDriveToolKit containing- googledrivecreatfile,googledrivesearchtool,googledrivereadfiletool etc


from langchain_core.tools import tool

#define functions
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
#define class for toolkit
class MathToolkit:
    def get_tools(self):
        return [add, multiply] #the functions you want to keep in toolkit

#create an obj of toolkit
toolkit=MathToolkit()
tools=toolkit.get_tools()
for tool in tools:
    print(tool.name,tool.description)
