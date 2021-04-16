from ui.ui import UI
from repositories.course_repository import CourseRepository
from database_connection import get_database_connection

class HomeMenu:
    def __init__(self,username):
        self._actions = {
            "x": "x Lopeta",
            "1": "1 Uusi kurssi",
            "2": "2 Hae kurssit"
        }
        self._headers = [
            "Kurssi",
            "Opintopisteet"
        ]
        self._ui = UI()
        self._repository = CourseRepository(get_database_connection())
        self._username = username

    def start(self):
        self._help()
        
        while True:
            action = self._ui.read("Anna komento: ")

            if not action in self._actions:
                self._ui.write("virheellinen komento")
                self._help()
                continue

            if action == "1":
                self._get_courses()
            elif action == "1":
                self._new_course()
            elif action == "x":
                break

    def _new_course(self):
        name = self._ui.read("Anna kurssinimi: ")
        credit = self._ui.read("Anna opintopisteet: ")
        self._repository.create(name, credit)

    def _get_courses(self):
        self._ui.write("{:<15}{:<18}".format(
            self._headers[0], self._headers[1]))
        for i in self._repository.get():
            self._ui.write("{:<15}{:<18}".format(i.course_name, i.credit))

    def _help(self):
        for i in self._actions:
            self._ui.write(self._actions[i])
