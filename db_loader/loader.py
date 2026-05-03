import sqlite3


def create_db():
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word VARCHAR(50) NOT NULL,
            translation VARCHAR(50) NOT NULL
        )
    ''')

    conn.commit()
    return conn


def load_db(connection):
    with open('words.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        cursor = connection.cursor()
        for line in lines:
            word, translation = line.split(':')
            print(f'Adding {word}:{translation}')
            cursor.execute(
                'INSERT INTO words (word, translation) VALUES (?, ?)', (word, translation))
        connection.commit()


def main():
    connection = create_db()
    load_db(connection)
    connection.close()

if __name__ == "__main__":
    main()