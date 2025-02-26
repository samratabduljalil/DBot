# 🚀 CRUD Functions
from sqlalchemy import  text
from database_conn import engine

def insert_data(query: str):
    """Executes an INSERT query."""
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    return "Insert operation successful."

def delete_data(query: str):
    """Executes a DELETE query."""
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    return "Delete operation successful."

def update_data(query: str):
    """Executes an UPDATE query."""
    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()
    return "Update operation successful."

def select_data(query: str):
    """Executes a SELECT query and returns results."""
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()