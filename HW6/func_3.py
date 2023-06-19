documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
    ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }

def get_name(doc_number):
    for numb in documents:
        if doc_number == numb["number"]:
            return numb['name']
    else:
        return "Документ не найден"

def get_directory(doc_number):
    for d_numb in directories:
        if doc_number in directories[d_numb]:
            return d_numb
    else:
        return "Полки с таким документом не найдено"

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))