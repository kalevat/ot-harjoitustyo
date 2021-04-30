import hashlib
from entities.courses import Courses

def courses_by_row(row):
    """Kurssitietojen ryhmitys

    Args:
        row: kurssitiedot tauluna

    Returns:
        kurssitiedot riveittäin
    """
    return Courses(row['course_name'], row['credit'], row['date']) if row else None


class CourseRepository:
    """Tietokannan käsittelystä vastaava luokka"""

    def __init__(self, connection):
        """Luokan konstruktori. Luo tietokantayhteyden"""

        self._connection = connection

    def create(self, name, credit):
        """Luo uuden kurssin

        Args:
            name: kurssinimi
            credit: opintopisteiden määrä

        Returns:
            kurssinimi
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'insert into courses (course_name, credit) values (?, ?)',
            (name, credit)
        )
        self._connection.commit()
        return name

    def get(self):
        """Hakee kaikki kurssit

        Returns:
            Kurssit tauluna
        """

        cursor = self._connection.cursor()
        cursor.execute('select * from courses')
        row = cursor.fetchall()
        return list(map(courses_by_row, row))

    def one_course(self,name):
        """Hakee yhden kurssi

        Args:
            name: kurssinimi

        Returns:
            tiedot rivinä
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from courses where course_name = ?',
            (name,)
        )
        row = cursor.fetchall()
        return row

    def delete_one(self,name):
        """Poistaa yhden kurssi

        Args:
            name: kurssinimi

        Returns:
            poiston tulos
        """

        cursor = self._connection.cursor()
        result= cursor.execute(
            'delete from courses where course_name =?',
            (name,)
        )
        self._connection.commit()
        return result

    def change(self,name,credit):
        """Vaihtaa kurssin opintopisteet

        Args:
            name: kurssinimi
            credit: opintopisteet

        Returns:
            kurssinimi
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'update courses set credit=? where course_name=?',
            (credit,name)
        )
        self._connection.commit()
        return name

    def delete_all(self):
        """Poistaa kaikki tiedot tietokannasta"""

        cursor = self._connection.cursor()
        cursor.execute('delete from courses')
        self._connection.commit()
        cursor.execute('delete from users')
        self._connection.commit()
        cursor.execute('delete from register')
        self._connection.commit()

    def new_user(self, username, password):
        """Uuden käyttäjän lisääminen

        Args:
            username: käyttäjänimi
            password: salasana

        Returns:
            käyttäjänimi
        """

        cursor = self._connection.cursor()
        hash_password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (username, hash_password)
        )
        self._connection.commit()
        return username

    def find_user(self,username):
        """Etsii käyttäjän tiedot tietokannasta

        Args:
            username: käyttäjänimi

        Returns:
            tiedot rivinä
        """

        cursor = self._connection.cursor()
        cursor.execute('select * from users where username=?',(username,))
        row = cursor.fetchall()
        return row

    def find_password(self,username,password):
        """Tarkistaa käyttäjän salasanan

        Args:
            username: käyttäjänimi
            password: salasana

        Returns:
            tiedot rivinä
        """

        cursor = self._connection.cursor()
        hash_password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        cursor.execute(
            'select * from users where username=? AND password=?',
            (username,hash_password)
        )
        row = cursor.fetchall()
        return row

    def course_date(self,name,date):
        """Lisätään kurssille tenttipäivämäärä

        Args:
            name: kurssinimi
            date: tenttipäivämäärä

        Returns:
            kurssinimi
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'update courses set date=? where course_name=?',
            (date,name)
        )
        self._connection.commit()
        return name

    def register_course(self,name,username):
        """Kurssille registeröinti

        Args:
            name: kurssinimi
            username: käyttäjänimi

        Returns:
            kurssinimi
        """

        cursor = self._connection.cursor()
        sql= """
            insert into register (name_id,course_id)
            values ((select id from users where username=?),
            (select id from courses where course_name=?))
            """
        cursor.execute(sql,(username,name))
        self._connection.commit()
        return name

    def my_exam(self,username,date):
        """Käyttäjän tulevat kurssi

        Args:
            username: käyttäjänimi
            date: today päivämäärä

        Returns:
            tulos rivinä
        """

        cursor = self._connection.cursor()
        sql = """
            select c.course_name, c.date from register r
            inner join courses c on c.id=r.course_id
            where r.name_id=(select id from users where username=?)
            AND c.date>=?
            """
        cursor.execute(sql,(username,date))
        row = cursor.fetchall()
        return row
        