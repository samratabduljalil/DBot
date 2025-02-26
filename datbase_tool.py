# ✅ CRUD Tools
from langchain.tools import Tool
from databse_function import insert_data, delete_data , update_data ,select_data
insert_tool = Tool(name="Insert Data", func=insert_data, description="Inserts data into the database. Provide a valid SQL INSERT statement.")
delete_tool = Tool(name="Delete Data", func=delete_data, description="Deletes data from the database. Provide a valid SQL DELETE statement.")
update_tool = Tool(name="Update Data", func=update_data, description="Updates records in the database. Provide a valid SQL UPDATE statement.")
select_tool = Tool(name="Select Data", func=select_data, description="Fetches records from the database. Provide a valid SQL SELECT statement.")
