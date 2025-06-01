import sqlite3
from typing import List, Optional

DB_PATH = 'barbershop_db.db'
SQL_PATH = r'C:\Main\my_projects\python_413\my_homeworks\SQL_week_4\barbershop.sql'

def sql_file_read(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def execute_script(conn: sqlite3.Connection, script: str) -> None:
    with conn:
        conn.executescript(script)

def find_appointment_by_phone(conn: sqlite3.Connection, phone: str) -> List[tuple]:
    query = '''
    SELECT a.id, c.name, c.phone, b.name, a.comment, a.created_at
    FROM appointments a
    JOIN clients c ON a.client_id = c.id
    JOIN barbers b ON a.barber_id = b.id
    WHERE c.phone = ?;
    '''
    return conn.execute(query, (phone,)).fetchall()

def find_appointment_by_comment(conn: sqlite3.Connection, comment_part: str) -> List[tuple]:
    query = '''
    SELECT a.id, c.name, c.phone, b.name, a.comment, a.created_at
    FROM appointments a
    JOIN clients c ON a.client_id = c.id
    JOIN barbers b ON a.barber_id = b.id
    WHERE a.comment LIKE ?;
    '''
    return conn.execute(query, (f'%{comment_part}%',)).fetchall()

def create_appointment(conn: sqlite3.Connection, client_name: str, client_phone: str, barber_name: str, services_list: List[str], comment: Optional[str] = None) -> int:
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM clients WHERE phone = ?', (client_phone,))
    client = cursor.fetchone()
    if client is None:
        cursor.execute('INSERT INTO clients (name, phone) VALUES (?, ?)', (client_name, client_phone))
        client_id = cursor.lastrowid
    else:
        client_id = client[0]

    cursor.execute('SELECT id FROM barbers WHERE name = ?', (barber_name,))
    barber = cursor.fetchone()
    if barber is None:
        raise ValueError(f'Барбер с именем "{barber_name}" не найден')
    barber_id = barber[0]

    cursor.execute(
        'INSERT INTO appointments (client_id, barber_id, comment) VALUES (?, ?, ?)',
        (client_id, barber_id, comment)
    )
    appointment_id = cursor.lastrowid

    for service_name in services_list:
        cursor.execute('SELECT id FROM services WHERE name = ?', (service_name,))
        service = cursor.fetchone()
        if service is None:
            raise ValueError(f'Услуга с именем "{service_name}" не найдена')
        service_id = service[0]
        cursor.execute(
            'INSERT INTO appointments_services (appointment_id, service_id) VALUES (?, ?)',
            (appointment_id, service_id)
        )
    
    conn.commit()
    return appointment_id

if __name__ == '__main__':
    conn = sqlite3.connect(DB_PATH)

    read_sql = sql_file_read(SQL_PATH)
    execute_script(conn, read_sql)

    print('Поиск по телефону "89991112233":')
    print(find_appointment_by_phone(conn, '89991112233'))

    print('\nПоиск по части комментария "стилёчек":')
    print(find_appointment_by_comment(conn, 'стилёчек'))

    print('\nСоздание новой записи...')
    new_appointment_id = create_appointment(
        conn,
        client_name='Алексей',
        client_phone='89991235555',
        barber_name='Аркадий',
        services_list=['Стрижка', 'Укладка'],
        comment='Хочу новую причёску'
    )
    print(f'Создана запись с ID: {new_appointment_id}')

    conn.close()