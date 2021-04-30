import datetime
from ui.ui import UI
from repositories.course_repository import CourseRepository
from database_connection import get_database_connection

class HomeMenu:
    """Päävalikon logiikasta vastaava luokka
    Attributes:
        username: kirjautuneen käyttäjän nimi
    """

    def __init__(self,username):
        """Luokan konstruktori. Luo päävalikon valinnat
        Args:
            username: kirjautuneen käyttäjän nimi
        """
        self._actions = {
            "x": "x Lopeta",
            "1": "1 Uusi kurssi",
            "2": "2 Hae kurssit",
            "3": "3 Poista kurssi",
            "4": "4 Muuta tietoja",
            "5": "5 Syötä tenttipäivämäärä",
            "6": "6 Ilmoittaudu kurssille",
            "7": "7 Tulevat tenttini"
        }
        self._headers = [
            "Kurssi",
            "Opintopisteet"
        ]
        self._ui = UI()
        self._repository = CourseRepository(get_database_connection())
        self._username = username

    def start(self):
        """Päävalikko"""

        self._help()
        while True:
            action = self._ui.read("Anna komento: ")

            if not action in self._actions:
                self._ui.write("virheellinen komento")
                self._help()
                continue

            if action == "1":
                self._new_course()
            elif action == "2":
                self._get_courses()
            elif action == "3":
                self._delete_course()
            elif action == "4":
                self._change_course()
            elif action == "5":
                self._exam_date()
            elif action == "6":
                self._register_course()
            elif action == "7":
                self._my_exam()
            elif action == "x":
                break

    def _input_course(self):
        """Kurssin tarkistaminen tietokannasta

        Returns:
            Kurssin nimi
            jos ei löydy niin False
        """

        name = self._ui.read("Anna kurssinimi: ")
        if self._repository.one_course(name) == []:
            self._ui.write("Kurssia ei löydy")
            return False
        return name

    def _new_course(self):
        """Uuden kurssin luominen"""

        name = self._ui.read("Anna kurssinimi: ")
        credit = self._ui.read("Anna opintopisteet: ")
        self._repository.create(name, credit)

    def _get_courses(self):
        """Kurssitietojen haku"""

        self._ui.write("{:<15}{:<18}".format(
            self._headers[0], self._headers[1]))
        for i in self._repository.get():
            self._ui.write("{:<15}{:<18}".format(i.course_name, i.credit))

    def _delete_course(self):
        """Kurssin poistaminen"""

        name=self._input_course()
        if name is not False:
            self._repository.delete_one(name)

    def _change_course(self):
        """Kurssin opintopisteiden vaihtaminen"""

        name=self._input_course()
        if name is not False:
            credit = self._ui.read("Anna uudet opintopisteet: ")
            self._repository.change(name,credit)

    def _exam_date(self):
        """Kurssin tenttipäivän lisääminen"""

        name=self._input_course()
        if name is not False:
            date = self._ui.read("Anna tenttipäivämäärä dd/mm/yyyy: ")
            day,month,year = date.split('/')
            try:
                datetime.datetime(int(year),int(month),int(day))
            except ValueError:
                self._ui.write("Väärä päivämäärä")
                return
            self._repository.course_date(name,year+month+day)

    def _register_course(self):
        """Kurssille rekisteröinti"""

        name=self._input_course()
        if name is not False:
            self._repository.register_course(name,self._username)

    def _my_exam(self):
        """Käyttäjän tulevat kurssit"""

        date=datetime.datetime.today().strftime('%Y%m%d')
        for i in self._repository.my_exam(self._username,date):
            self._ui.write("{:<15}{:<18}".format(i[0], i[1][6:8]+"/"+i[1][4:6]+"/"+i[1][2:4]))

    def _help(self):
        """Päävalikko"""

        for i in self._actions:
            self._ui.write(self._actions[i])
