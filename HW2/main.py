from pprint import pprint
import csv
import re
import os

# 1. Выполните пункты 1-3 задания.
def sort(contact_list):
    """сортируем и приводим в порядок"""
    spis = len(contact_list[0])
    for index, contact in enumerate(contact_list):
        contact_list[index] = contact[:spis]

def search(contact_list):
    """функция по поиску ФИО"""
    for fio in contact_list[1:]:
        pattern = re.search(r"([А-ЯЁ][а-яё]+)[, ]?([А-ЯЁ][а-яё]+)[, ]?([А-ЯЁ][а-яё]+)?", ' '.join(fio[:3]).strip())
        fio[0], fio[1], fio[2] = pattern.group(1), pattern.group(2), pattern.group(3)

def phone_sub(contact_list):
    """функция по поиску и приведению телефонов к единому стандарту"""
    for phone in contact_list[1:]:
        phone[5] = re.sub(r'(\+?[7|8])? ?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})\s?\(?(доб.\)?)?\s?(\d{4})?\)?', r'+7(\2)\3-\4-\5 \6\7', phone[5])
        phone[5] = phone[5].strip()

def association(contact_list):
    """объединяем всех с одинаковой фамилией"""
    contac = {}
    end_list = [contact_list[0]]
    for index, cont in enumerate(contact_list[1:]):
        if cont[0] not in contac.keys():
            contac[cont[0]] = index + 1
        else:
            fix = contact_list[contac[cont[0]]]
            for i in range(1, 7):
                fix[i] = fix[i] or cont[i]
    for index in contac.values():
        end_list.append(contact_list[index])
    return end_list


if __name__ == "__main__":
    path = os.path.dirname(__file__)

    with open(path + "/phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)


        sort(contacts_list)
        search(contacts_list)
        phone_sub(contacts_list)
        contacts_list = association(contacts_list)
        pprint(contacts_list)

    with open(path + "/phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)