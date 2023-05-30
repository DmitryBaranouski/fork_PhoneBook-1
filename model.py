def get_data():  # открытие
    with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')[:-1]
        return data

def storage():
    with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
        print(file.read(), end="")

def add_contact(name, phone):  # запись в файл
    with open('PhoneBook.txt', 'a', encoding='utf-8') as file:
        file.write(name + ':' + phone + '\n')


def find(contact):  # вывод искомого контаката
    with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if contact in line:
                print(line.strip())
            else:
                print('Контакт не найден')

def show_search(contact, new_contact):
    with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
        old_file = file.read()
        new_file = old_file.replace(contact, new_contact)
    with open('Phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(new_file)

def delete_contact(contact):
    with open('PhoneBook.txt', 'r', encoding='utf-8') as file:
        old_file = file.read()
        new_file = old_file.replace(contact, ' ')
    with open('Phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(new_file)