import sqlite3
from typing import List

DB_PATH = 'barbershop_db.db'
SQL_PATH = 'barbershop.sql'

def sql_file_read(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def execute_script(conn: sqlite3.Connection, script: str) -> None:
    with conn:
        conn.executescript(script)

