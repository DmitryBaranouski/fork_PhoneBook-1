def greetings():
    return None


def menu():
    print(
        '1 – Показать все контакты\n'
        '2 – Добавить контакт\n'
        '3 – Найти контакт\n'
        '4 – Редактировать контакт\n'
        '5 – Удалить контакт\n'
        '6 – Выход'
    )

def error():
    print('\nВведите корректный запрос!!!\n')
    return None

def result(result):
    print('Контакт успешно сохранен!''\n')

def show_contacts(data):
    print(data)

def not_find(contact):
    print('Контакт не найден')

def show_search(res):
    print('Контакт успешно изменен')

def delete_contact(res):
    print('Контакт удален')

    return None


if name == 'main':
    menu()