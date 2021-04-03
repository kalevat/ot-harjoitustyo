import unittest
from repositories.course_repository import CourseRepository
from entities.courses import Courses
from database_connection import get_database_connection


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.course = CourseRepository(get_database_connection())
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

