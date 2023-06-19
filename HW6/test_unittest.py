from func_1 import solution
from func_2 import vote
from func_3 import get_name, get_directory
from yandex_api import header, name_papka_unittest, create
from TOKEN import TOKEN
import unittest
from unittest import TestCase


class Test_func_1(TestCase):
    def test_numbers_1(self):
        self.assertEqual(solution(1, 8, 15), (-3.0, -5.0))
        self.assertEqual(solution(1, -13, 12), (12.0, 1.0))
        self.assertEqual(solution(-4, 28, -49), 3.5)
        self.assertEqual(solution(1, 1, 1), "корней нет")


class Test_func_2(TestCase):
    def test_numbers_2(self):
        self.assertEqual(vote([1, 2, 1, 2, 3]), 1)
        self.assertEqual(vote([1, 2, 3, 2, 2]), 2)


class Test_func_3(TestCase):
    def test_numbers_3(self):
        doc = "11-2"
        res = get_directory(doc)
        self.assertEqual(res, "1")

        doc = "10006"
        res = get_name(doc)
        self.assertEqual(res, "Аристарх Павлов")

class Test_func_4_yandex(TestCase):
    def test_create_folder_status_code(self):
        status_code = create(name_papka_unittest)
        self.assertIn(status_code, [201])

if __name__ == "__main__":
    unittest.main()
