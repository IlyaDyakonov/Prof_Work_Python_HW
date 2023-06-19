from func_1 import solution
from func_2 import vote
from func_3 import get_name, get_directory
import pytest
from yandex_api import header, name_papka_pytest, create
from TOKEN import TOKEN



def test_func_1():
    assert solution(1, 8, 15) == (-3.0, -5.0)
    assert solution(1, -13, 12) == (12.0, 1.0)
    assert solution(-4, 28, -49) == 3.5
    assert solution(1, 1, 1) == "корней нет"


def test_func_2():
    assert vote([1, 1, 1, 2, 3]) == 1
    assert vote([1, 2, 3, 2, 2]) == 2


def test_func_3():
    assert get_name("2207 876234") == "Василий Гупкин"
    assert get_name("10006") == "Аристарх Павлов"
    assert get_name("5455 028765") == "Василий Иванов"
    assert get_name("12345") == "Документ не найден"
    assert get_name("99999") == "Документ не найден"
    assert get_directory("2207 876234") == "1"
    assert get_directory("10006") == "2"
    assert get_directory("5455 028765") == "1"
    assert get_directory("12345") == "Полки с таким документом не найдено"
    assert get_directory("99999") == "Полки с таким документом не найдено"

class Test_Yandex_API:
    def test_create_folder_status_code(self):
        status_code = create(name_papka_pytest)
        assert status_code in [201]


