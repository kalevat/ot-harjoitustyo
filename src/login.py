from ui.ui import UI
from repositories.course_repository import CourseRepository
from database_connection import get_database_connection

class LoginMenu:
    def __init__(self):
        self._ui = UI()
        self._repository = CourseRepository(get_database_connection())

    def login(self):
        username=""
        while username=="":
            username = self._ui.read("Anna käyttäjätunnus: ")
        result = self._repository.find_user(username)
        if result == []:
            self._ui.write("Ei tunnusta valmiina")
            self._singup(username)
            self.login()
        else:
            result=[]
            while result==[]:
                password = self._ui.read_password("Anna salasana: ")
                result = self._repository.find_password(username,password)
        return username

    def _singup(self,username):
        result = self._ui.read("Haluatko luoda tunnuksen k/e: ")
        if result == "k":
            password_check=False
            while password_check is False:
                password=self._ui.read_password("Anna uusi salasana: ")
                if len(password)>4:
                    password_check=True
                else:
                    self._ui.write("Liian lyhyt salasana")
            self._repository.new_user(username, password)
