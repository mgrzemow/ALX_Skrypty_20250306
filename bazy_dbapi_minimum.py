# biblioteki - standard dbapi2.0
# konkretna biblioteka - z dokumentacji do bazy

import sqlite3

if __name__ == '__main__':
    with sqlite3.connect(':memory:') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1, 2, 3')
        for r in cursor:
            print(r)
