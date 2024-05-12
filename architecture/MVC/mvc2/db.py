import sqlite3

def execute(query):
    db_path = './geek.university'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
    except Exception as e:
        print(f'Error during query execution: {e}')