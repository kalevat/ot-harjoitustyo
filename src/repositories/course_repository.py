from database_connection import get_database_connection
from entities.courses import Courses


def courses_by_row(row):
    return Courses(row['course_name'], row['credit']) if row else None


class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, credit):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into courses (course_name, credit) values (?, ?)',
            (name, credit)
        )
        self._connection.commit()
        return name

    def get(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from courses')
        row = cursor.fetchall()
        return list(map(courses_by_row, row))

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from courses')
        self._connection.commit()
