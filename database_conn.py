from sqlalchemy import create_engine, text
from langchain.sql_database import SQLDatabase
# Database Connection
DATABASE_URL = "mysql+pymysql://root@localhost/DBot"  # Modify if needed
engine = create_engine(DATABASE_URL)
db = SQLDatabase(engine)