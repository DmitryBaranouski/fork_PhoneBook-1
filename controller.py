import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        print()
        if answer == '1':
            print('Список контактов: ')
            data = model.storage()
            view.show_contacts(data)
        elif answer == '2':
            print('Введите данные нового контакта')
            contact, phone = input('Имя: ').capitalize(), input(
                "номер телефона:  ")
            result = model.add_contact(contact, phone)
            view.result(result)

        elif answer == '3':
            contact = input("Введите данные контакта для поиска: ")
            res = model.find(contact)
            view.show_contacts(res)
        elif answer == '4':
            contact = input('Имя контакта,который хотите изменить: ')
            new_contact = input('Введите актуальные данные: ')
            res = model.show_search(contact, new_contact)
            view.show_search(res)

        elif answer == '5':
            contact = input('Ведите данные контакта, который хотите удалить: ')
            res = model.delete_contact(contact)
            view.delete_contact(res)

        elif answer == '6':
            view.ciao()
        else:
            view.error()