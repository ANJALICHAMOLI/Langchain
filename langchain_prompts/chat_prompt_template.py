from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])


prompt = chat_template.invoke({'domain':'AI','topic':'layers of ai in breif'})

print(prompt)
