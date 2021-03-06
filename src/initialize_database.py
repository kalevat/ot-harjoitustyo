from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists courses;
    ''')

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists register;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table courses (
            id integer primary key,
            course_name text, credit int, date text
        );
    ''')

    cursor.execute('''
        create table users (
            id integer primary key,
            username text, password text
        );
    ''')

    cursor.execute('''
        create table register (
            id integer primary key,
            name_id int, course_id int
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

# This allows us to call the initialize_database function using command line
if __name__ == "__main__":
    initialize_database()
    