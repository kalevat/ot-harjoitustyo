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
        cursor.execute('delete from users')
        self._connection.commit()
        cursor.execute('delete from register')
        self._connection.commit()

    def new_user(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (username, password)
        )
        self._connection.commit()
        return username

    def find_user(self,username):
        cursor = self._connection.cursor()
        cursor.execute('select * from users where username=?',(username,))
        row = cursor.fetchall()
        return row

    def find_password(self,username,password):
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users where username=? AND password=?',
            (username,password)
        )
        row = cursor.fetchall()
        return row
        