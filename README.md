# 🤖 Generative AI & LangChain

<p align="center">
  <img src="https://img.shields.io/badge/Generative%20AI-Learning-8B5CF6?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" />
  <img src="https://img.shields.io/badge/RAG-FF6B6B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI%20Agents-00A67E?style=for-the-badge" />
</p>

<p align="center">
  <b>Hands on learning and implementation of Generative AI, LangChain, RAG, Tool Calling and AI Agents.</b>
</p>

---

# 🛠️ Tech Stack

## Languages

<p>
  <img src="https://skillicons.dev/icons?i=python,java,html,css" />
</p>

---

## 🤖 Generative AI

<p>
  <img src="https://skillicons.dev/icons?i=python" />
</p>

- Large Language Models (LLMs)
- Prompt Engineering
- Chat Models
- Embeddings
- Generative AI Applications
- Tool Calling
- AI Agents
- ReAct Agents

---

## 🔗 LangChain

<p>
  <img src="https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" />
</p>

- LangChain Fundamentals
- Models
- Prompt Templates
- Chains
- Documents
- Retrievers
- Vector Stores
- Tool Binding
- Tool Calling
- Tool Execution
- Agents
- AgentExecutor
- ReAct

---

## 📚 RAG — Retrieval Augmented Generation

<p>
  <img src="https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-8B5CF6?style=for-the-badge" />
</p>

- Document Retrieval
- Embeddings
- Similarity Search
- Vector Store Retrieval
- Source-Based Retrieval
- Wikipedia Retrieval
- FAISS Retrieval
- MMR Retrieval
- MultiQuery Retrieval

### RAG Architecture

```text
Documents
    ↓
Document Processing
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retriever
    ↓
Relevant Documents
    ↓
LLM
    ↓
Response
```

----
## 🗃️ Vector Stores

<p align="left">
  <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Chroma-FF6B35?style=for-the-badge" />
</p>

- FAISS
- Chroma
- Vector Embeddings
- Similarity Search
- Retriever Interfaces

---

## 🔎 Retrievers

### Wikipedia Retriever

<p>
  <img src="https://img.shields.io/badge/Wikipedia-Retriever-000000?style=for-the-badge&logo=wikipedia&logoColor=white" />
</p>

- Wikipedia API
- `WikipediaRetriever`
- Source-Based Retrieval
- Retrieved Documents
- Metadata

### MMR Retriever

<p>
  <img src="https://img.shields.io/badge/MMR-Maximal%20Marginal%20Relevance-4F46E5?style=for-the-badge" />
</p>

- Relevance
- Diversity
- MMR-based document selection

### MultiQuery Retriever

<p>
  <img src="https://img.shields.io/badge/MultiQuery-Retrieval-9333EA?style=for-the-badge" />
</p>

- Query Expansion
- Multiple Semantic Queries
- Retrieval for Multiple Queries
- Result Merging
- Duplicate Removal

---

## 📺 YouTube Transcript Processing

<p>
  <img src="https://img.shields.io/badge/YouTube-Transcript%20API-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
</p>

- YouTube Transcript API
- Video ID extraction
- Transcript retrieval
- Transcript snippet processing
- Converting transcript snippets into plain text

### Workflow

```text
YouTube Video
      ↓
Video ID
      ↓
YouTube Transcript API
      ↓
Transcript Snippets
      ↓
Plain Text
```

---

# 🧰 Tools & Tool Calling

<p>
  <img src="https://img.shields.io/badge/Tools-LangChain-1C3C3C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tool%20Calling-LLM%20Functions-00A67E?style=for-the-badge" />
</p>

## Custom Tools

Implemented custom tools using:

```python
@tool
```

Example:

```python
@tool
def multiply(a: int, b: int) -> int:
    """Returns the product of two numbers."""
    return a * b
```

### Concepts Covered

- Custom Tools
- Structured Tools
- Tool Schemas
- Type Annotations
- Pydantic Validation
- `InjectedToolArg`
- Tool Binding
- Tool Calls
- Tool Execution

---

# 🔗 Tool Binding

Tool binding connects tools with an LLM.

```text
Tool
  ↓
bind_tools()
  ↓
LLM
```

Example:

```python
llm_with_tools = llm.bind_tools([multiply])
```

The LLM can then determine when a tool should be called.

---

# 📞 Tool Calling

The LLM does not directly execute the Python function.

Instead:

```text
User
 ↓
LLM
 ↓
AIMessage
 ↓
tool_calls
 ↓
Tool Execution
 ↓
Tool Result
 ↓
LLM
 ↓
Final Response
```

Worked with:

```python
ai_message.tool_calls
```

and:

```python
tool.invoke(...)
```

---

# ⚙️ Tool Execution

Explored the complete manual tool execution process.

```text
HumanMessage
      ↓
LLM
      ↓
AIMessage
      ↓
Tool Call
      ↓
Execute Tool
      ↓
Tool Message
      ↓
Append Result
      ↓
LLM
      ↓
Final Answer
```

This helped understand what happens behind higher-level agent abstractions.

---

# 💱 Currency Conversion Tool

Built a currency conversion tool using an external exchange-rate API.

<p>
  <img src="https://img.shields.io/badge/API-Exchange%20Rate-2563EB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-Requests-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</p>

### Workflow

```text
User Query
     ↓
LLM
     ↓
get_conversion_factor
     ↓
Exchange Rate API
     ↓
Conversion Rate
     ↓
convert
     ↓
Final Value
```

### Concepts Covered

- External API integration
- API Keys
- Environment Variables
- `requests`
- Multiple tool calls
- Passing output from one tool into another
- `Annotated`
- `InjectedToolArg`

---

# 🧩 Structured Tools

Worked with structured tool inputs and typed arguments.

### Concepts

- `StructuredTool`
- Type hints
- `Annotated`
- `InjectedToolArg`
- Pydantic schemas
- Structured tool arguments
- Tool input validation

---

# 🧠 AI Agents

<p>
  <img src="https://img.shields.io/badge/AI%20Agents-Agentic%20AI-00A67E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ReAct-Reason%20%2B%20Act-F59E0B?style=for-the-badge" />
</p>

Learned how agents use an LLM together with tools to accomplish multi-step tasks.

### Agent Workflow

```text
User Goal
    ↓
LLM
    ↓
Choose Tool
    ↓
Execute Tool
    ↓
Observation
    ↓
LLM
    ↓
Choose Next Action
    ↓
Execute Tool
    ↓
Final Answer
```

---

# 🔄 ReAct Agents

Explored the **Reason + Act** pattern.

```text
Thought
   ↓
Action
   ↓
Action Input
   ↓
Observation
   ↓
Thought
   ↓
Action
   ↓
Observation
   ↓
Final Answer
```

The agent can use the result of one action to determine what it should do next.

---

# 🌐 Multi-Tool Agent

Built an agent capable of handling a multi-step question:

> Find the capital of India, then find its current weather condition.

The agent was provided with multiple tools including:

- DuckDuckGo Search
- Weather Tool

### Agent Flow

```text
User Question
      ↓
DuckDuckGo Search
      ↓
New Delhi
      ↓
Weather Tool
      ↓
Weather Information
      ↓
Final Answer
```

It also demonstrated fallback behavior when the weather API failed.

---

# 🌍 APIs & Environment Variables

<p>
  <img src="https://skillicons.dev/icons?i=python" />
</p>

Worked with external APIs and API authentication.

### Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

Used environment variables for:

- Google API keys
- Groq API keys
- Exchange-rate API keys
- Model configuration

API keys are kept outside source code using `.env`.

---

# 🤖 LLM Providers

## Google Gemini

<p>
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" />
</p>

Used for:

- LLM applications
- Embeddings
- Vector retrieval
- RAG experiments

---

## Groq

<p>
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" />
</p>

Used for:

- Chat models
- Tool calling
- Tool execution
- AI agents

---

# 🛠️ Development Tools

<p>
  <img src="https://skillicons.dev/icons?i=git,github,vscode" />
</p>

### Version Control

- Git
- GitHub
- Branching
- Commits
- Push / Pull
- Repository management

### Development

- VS Code
- Python Virtual Environments
- `.env`
- Debugging
- API testing

---

# 📦 Libraries & Frameworks

<p align="left">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=chainlink&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain%20Community-1C3C3C?style=flat-square" />
  <img src="https://img.shields.io/badge/FAISS-0467DF?style=flat-square" />
  <img src="https://img.shields.io/badge/Chroma-FF6B35?style=flat-square" />
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat-square&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=flat-square" />
  <img src="https://img.shields.io/badge/Requests-2CA5E0?style=flat-square" />
  <img src="https://img.shields.io/badge/Python%20Dotenv-ECD53F?style=flat-square" />
</p>

---

# 📊 Concepts Covered

| Concept | Status |
|---|:---:|
| LLMs | ✅ |
| Chat Models | ✅ |
| Prompting | ✅ |
| Embeddings | ✅ |
| RAG | ✅ |
| Wikipedia Retriever | ✅ |
| FAISS | ✅ |
| Chroma | ✅ |
| Similarity Search | ✅ |
| MMR Retriever | ✅ |
| MultiQuery Retriever | ✅ |
| YouTube Transcript API | ✅ |
| Custom Tools | ✅ |
| Structured Tools | ✅ |
| Tool Binding | ✅ |
| Tool Calling | ✅ |
| Tool Execution | ✅ |
| External APIs | ✅ |
| ReAct | ✅ |
| AI Agents | ✅ |
| AgentExecutor | ✅ |

---

# 🧠 What This Repository Represents

This repository contains my practical implementations and experiments while learning **Generative AI and LLM application development**.

The focus is on understanding how the individual components work together:

```text
LLM
 ↓
Embeddings
 ↓
RAG
 ↓
Retrieval
 ↓
Vector Stores
 ↓
Tools
 ↓
Tool Calling
 ↓
Tool Execution
 ↓
Agents
```

<p align="center">
  <b>Learning by building, debugging, and understanding how things work under the hood. 🚀</b>
</p>
