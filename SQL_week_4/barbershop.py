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

def find_appointment_by_phone(conn: sqlite3.Connection, phone: str) -> List[tuple]:
    query = '''
    SELECT a.id, c.name, c.phone, m.name, a.comment, a.created_at
    FROM appointment a
    JOIN client c ON a.client_id = c.id
    JOIN master m ON a.master_id = m.id
    WHERE c.phone = ?;
    '''
    return conn.execute(query, (phone,)).fetchall()

def find_appointment_by_comment(conn: sqlite3.Connection, comment_part: str) -> List[tuple]:
    query = '''
    SELECT a.id, c.name, c.phone, m.name, a.comment, a.created_at
    FROM appointment a
    JOIN client c ON a.client_id = c.id
    JOIN master m ON a.master_id = m.id
    WHERE a.comment LIKE ?;
    '''
    return conn.execute(query, (f'%{comment_part}%',)).fetchall()