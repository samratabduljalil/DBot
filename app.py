from fastapi import FastAPI, Query
from langchain.llms import Ollama
from database_conn import db
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from datbase_tool import insert_tool, delete_tool, update_tool, select_tool
from prompt import enhanced_prompt
from langchain.agents import AgentExecutor
# FastAPI Initialization
app = FastAPI(title="SQL Agent API", description="An enhanced SQL Agent API using Ollama and LangChain.")



# Ollama server details
OLLAMA_URL = "http://127.0.0.1:12345"

# Initialize Ollama LLM
ollama_llm = Ollama(model="llama3:latest", base_url=OLLAMA_URL, temperature=0)

# ✅ Create SQL Agent with Full Toolset
# 🚀 Create SQL Agent with Tools (Forcing Function Execution)
sql_agent = create_sql_agent(
    llm=ollama_llm,
    db=db,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    extra_tools=[insert_tool, delete_tool, update_tool, select_tool]  # ✅ Ensure tools are correctly attached
)
agent_executor = AgentExecutor(agent=sql_agent, tools=[insert_tool, delete_tool, update_tool, select_tool], verbose=True)
@app.get("/")
def home():
    return {"message": "Welcome to the Enhanced SQL Agent API with Full Tool Support"}

@app.get("/query")
def query_database(question: str = Query(..., description="Enter your natural language query")):
    try:
        response = sql_agent.invoke(question)
        return {"question": question, "response": response}
    except Exception as e:
        return {"error": str(e)}