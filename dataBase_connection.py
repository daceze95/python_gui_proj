import pyodbc
from dotenv import load_env 


DB_NAME=None #"database name"
TABLE_NAME=None#"database table name"
DRIVER=None#"ODBC Driver 17 for SQL Server"
SERVER=None#"hostname\server_instance"


connection = pyodbc.connect(f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB_NAME};Trusted_Connection=yes;")

# cursor=connection.cursor()
