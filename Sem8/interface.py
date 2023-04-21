def hello():
    print("Справочник\n1. Добавить контакт - 1\n2. Поиск контакта - 2\n3. Просмотр контактов - 3\n4. Изменить контакт - 4\n5. Удалить контакт - 5\n6. Закрыть - 0")
    a = input()
    return a

def get_contact():
    return [input('Имя: ')+" ", input('Фамилия: ')+" ", input('Отчество: ')+" ", input('Телефон: ')]

def get_search_contact():
    return input('Введите имя/фамилию: ')
