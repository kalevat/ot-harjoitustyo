import unittest
from repositories.course_repository import CourseRepository
from entities.courses import Courses
from database_connection import get_database_connection

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.course = CourseRepository(get_database_connection())
        self.users = CourseRepository(get_database_connection())
        self.course.delete_all()

    def test_create(self):
        self.course.create("english","2")
        courses = self.course.get()
        self.assertEqual(len(courses),1)
        self.assertEqual(courses[0].course_name,"english")
        self.assertEqual(courses[0].credit,2)

    def test_find_all(self):
        self.course.create("english","2")
        self.course.create("math","5")
        courses = self.course.get()
        self.assertEqual(len(courses),2)
        self.assertEqual(courses[0].course_name,"english")
        self.assertEqual(courses[0].credit,2)
        self.assertEqual(courses[1].course_name,"math")
        self.assertEqual(courses[1].credit,5)

    def test_find_one(self):
        self.course.create("english","2")
        courses = self.course.one_course("english")
        self.assertEqual(len(courses),1)

    def test_delete_one(self):
        self.course.create("swedish","2")
        self.course.delete_one("swedish")
        courses = self.course.one_course("swedish")
        self.assertEqual(len(courses),0)

    def test_change(self):
        self.course.create("history","2")
        self.course.change("history","4")
        courses = self.course.get()
        self.assertEqual(courses[0].credit,4)
       
    def test_course_date(self):
        self.course.create("english","3")
        self.course.course_date("english","20211230")
        courses = self.course.get()
        self.assertEqual(courses[0].date,"20211230")

    def test_register_course(self):
        self.course.create("english","3")
        self.users.new_user("tomi","salasana")
        self.course.register_course("english","tomi")
        self.course.course_date("english","20211231")
        register = self.course.my_exam("tomi","20210101")
        self.assertEqual(len(register),1)