from fastapi import FastAPI, Query
from langchain.llms import Ollama
from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.tools import Tool
from sqlalchemy import create_engine, text
import logging

# Initialize FastAPI
app = FastAPI(title="SQL Agent API", description="SQL Agent with Ollama and LangChain for CRUD operations.")

# Configure Logging
logging.basicConfig(level=logging.INFO)

# Database Connection
DATABASE_URL = "mysql+pymysql://root@localhost/dbot"  # Modify as needed
engine = create_engine(DATABASE_URL)
db = SQLDatabase(engine)

# Ollama LLM Configuration
OLLAMA_URL = "http://127.0.0.1:12345"
ollama_llm = Ollama(model="llama3:latest", base_url=OLLAMA_URL, temperature=0)

# CRUD Function Definitions
def insert_data(query: str):
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    return "✅ Insert successful."

def delete_data(query: str):
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    return "✅ Delete successful."

def update_data(query: str):
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    return "✅ Update successful."

def select_data(query: str):
    with engine.connect() as conn:
        result = conn.execute(text(query)).fetchall()
        data = [dict(row) for row in result] if result else []
        logging.info(f"SELECT Response: {data}")  # Debugging
        return data if data else "No results found."

# Define Tools for CRUD Operations
insert_tool = Tool(
    name="Insert Data",
    func=insert_data,
    description="Use this tool to insert new records into the database. Provide a valid SQL INSERT query."
)

delete_tool = Tool(
    name="Delete Data",
    func=delete_data,
    description="Use this tool to delete records from the database. Provide a valid SQL DELETE query."
)

update_tool = Tool(
    name="Update Data",
    func=update_data,
    description="Use this tool to update existing records in the database. Provide a valid SQL UPDATE query."
)

select_tool = Tool(
    name="Select Data",
    func=select_data,
    description="Use this tool to retrieve data from the database. Provide a valid SQL SELECT query."
)

# Create SQL Agent
sql_agent = create_sql_agent(
    llm=ollama_llm,
    db=db,
    agent_type=AgentType.OPENAI_FUNCTIONS,  # ✅ Forces the LLM to use tools
    verbose=True,
    tools=[insert_tool, delete_tool, update_tool, select_tool],  # ✅ Ensures tools are passed
)

# Create Agent Executor with Error Handling
agent_executor = AgentExecutor(
    agent=sql_agent,
    tools=[insert_tool, delete_tool, update_tool, select_tool],  # ✅ Ensures tools are recognized
    verbose=True,
    handle_parsing_errors=True  # ✅ Fixes output parsing error
)

# API Endpoints
@app.get("/")
def home():
    return {"message": "Welcome to the Enhanced SQL Agent API with Full CRUD Support"}

@app.get("/query")
def query_database(question: str = Query(..., description="Enter your natural language query")):
    try:
        logging.info(f"Received query: {question}")  # Debugging
        response = agent_executor.invoke({"input": question})  # ✅ Fix: Use invoke() correctly
        logging.info(f"Agent response: {response}")  # Debugging
        return {"question": question, "response": response}
    except Exception as e:
        logging.error(f"Error: {str(e)}")  # Log errors
        return {"error": str(e)}
