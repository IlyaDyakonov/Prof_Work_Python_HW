import requests
from fake_headers import Headers
import bs4
from tqdm import tqdm
import re
import json

headers = Headers(browser="firefox", os="win")
headers_data = headers.generate()
vacancys = []
count = 0
for page in tqdm(range(1, 41), desc="Выгружаем все вакансии....."):
    main_page_html = requests.get(
        "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={}".format(page),
        headers=headers_data).text
    main_page_soup = bs4.BeautifulSoup(main_page_html, "lxml")
    vacan = main_page_soup.find_all("div", class_="serp-item")

    for sear in vacan:
        all_link = sear.find('a') # ссылки
        link = all_link['href']

        salary = sear.find('span', class_="bloko-header-section-3") # зарплата
        sal = sear.text.strip()
        if salary:
            salary_text = salary.get_text(strip=True)
        else:
            salary_text = None

        name_vacan = sear.find(class_="bloko-header-section-3").text # название вакансии

        company_info = sear.find('div', class_='vacancy-serp-item-company') # сортировка по городам
        company_city = ""
        if company_info:
            company_text = company_info.get_text(strip=True)
            city_match = re.search(r'(?:Москва|Санкт-Петербург)', company_text)
            if city_match:
                company_city = city_match.group()

        vacancy = {
            'link': link,
            'salary': str(salary_text),
            'name': name_vacan,
            'city': company_city
        }

        response1 = requests.get(link, headers=headers_data) # проходим описание и выдёргиваем Django|Flask
        html_data1 = response1.text
        soup1 = bs4.BeautifulSoup(html_data1, 'lxml')
        tag1 = soup1.find('div', class_='g-user-content')
        if vacan:
            text = tag1.text
            match = re.search(r'\b(Django|Flask)\b', text)
            if match:
                match_word = match.group(0)
                print(match_word)
                vacancys.append(vacancy)
                count += 1
            else:
                continue


        # Записываем в файл результат парсинга с сохранением кодировки UTF-8
        filename = 'data_parsing.json'

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(vacancys, file, indent=4, ensure_ascii=False)

print(f'Кол-во найденых вакансий: {count}')