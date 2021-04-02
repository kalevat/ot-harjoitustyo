from database_connection import get_database_connection

class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, id):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into courses (name, credit) values (?, ?)',
            (name, id)
        )
        self._connection.commit()
        return name

    def get(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from courses')
        row = cursor.fetchall()
        return list(row)
