# 🚀 SQL Agent API with LangChain & Ollama

## 📌 Project Status: **Under Development** ⚠️

This project is an AI-powered SQL agent built using **FastAPI**, **LangChain**, and **Ollama** (running a local LLM like `llama3`). The agent enables **natural language interactions** with a MySQL database, supporting CRUD operations (INSERT, SELECT, UPDATE, DELETE) through AI-generated SQL queries.

---

## 🌟 Features
- 🧠 **AI-Powered SQL Agent**: Uses LangChain and Ollama to process natural language queries.
- ⚡ **FastAPI Backend**: Provides a RESTful API for easy integration.
- 🔍 **Full CRUD Support**: Insert, update, delete, and retrieve data using AI.
- 🛠 **Error Handling**: Handles parsing errors and ensures smooth execution.
- 📝 **Logging & Debugging**: Logs queries and responses for better transparency.
- 🎨 **Streamlit UI**: A simple frontend to interact with the SQL agent.

---

## 📦 Technologies Used
- **FastAPI** - Web framework for building APIs
- **LangChain** - AI-powered agent framework
- **Ollama** - Local LLM execution
- **MySQL** - Relational database
- **SQLAlchemy** - Database connection & ORM
- **Streamlit** - Web UI for interacting with the SQL agent

---

## 🚀 Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/samratabduljalil/DBot
cd sql-agent-api
```

### 2️⃣ **Set Up Conda Environment**
```bash
conda create -n sql-agent python=3.10 
conda activate sql-agent
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run Ollama LLM Locally**
Make sure you have [Ollama installed](https://ollama.ai/) and start the LLM server:
```bash
ollama pull llama3:latest  # Ensure the required model is downloaded
set OLLAMA_HOST=127.0.0.1:12345
ollama serve
```

### 5️⃣ **Set Up MySQL Database**
Modify the `DATABASE_URL` in `main.py` to match your MySQL credentials:
```python
DATABASE_URL = "mysql+pymysql://root@localhost/yourdatabase"
```
Ensure your MySQL server is running and the `yourdatabase` database exists.

### 6️⃣ **Run the API Server**
```bash
uvicorn main:app --reload
```
The API will be available at: **`http://127.0.0.1:8000`**

### 7️⃣ **Run the Frontend (Streamlit UI)**
Navigate to the frontend directory and run:
```bash
streamlit run app.py
```
This will launch the Streamlit UI where you can interact with the SQL Agent.

---


## 👨‍💻 Author
Developed by **Samrat Abdul Jalil**

---

## 📫 Contact
For any queries or contributions, feel free to reach out:
- GitHub: [@samratabduljalil](https://github.com/samratabduljalil)
- Email: samratabduljalil21@gmail.com




⚠️ **Note:** This project is still under active development. Expect frequent updates and improvements. 🚀

