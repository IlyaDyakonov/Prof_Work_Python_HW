from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from colorama import Fore, Back, Style

time_now = date.today()
date_color = 'Сегодняшняя дата: {date_now}'.format(date_now=Fore.LIGHTCYAN_EX + str(time_now) + Style.RESET_ALL)

if __name__ == '__main__':
    print(date_color)
    print()
    calculate_salary()
    print()
    get_employees()
    print()
    print(Fore.LIGHTYELLOW_EX + 'Пункт 4 из ДЗ.')
    print(Fore.MAGENTA + 'не сказать что особо программа...')
    print(Back.LIGHTCYAN_EX + 'но немного сможем поиграться с цветами))')
    print(Style.RESET_ALL)
