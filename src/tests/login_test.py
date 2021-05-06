import unittest
from repositories.course_repository import CourseRepository
from database_connection import get_database_connection
from login import LoginMenu


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.users = CourseRepository(get_database_connection())
        self.users.delete_all()
        self.login = LoginMenu
     
    def test_newuser(self):
        self.users.new_user("tomi","salasana")
        result = self.users.find_user("tomi")
        self.assertEqual(len(result),1)

    def test_password(self):
        self.users.new_user("tomi","salasana")
        result = self.users.find_password("tomi","salasana")
        self.assertEqual(len(result),1)
