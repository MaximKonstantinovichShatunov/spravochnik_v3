from function import init_dict, print_book, write_new_contact_list, write_new_contact_str
from function import delete_contact_str, delete_contact_list
from inputreplase import search


def print_hint():
    print('''\n                                                               
            - Просмотр всех записей обоих справочников:  - 1              
            - Добавление новой записи в строковый справочник: - 2         
            - Добавление новой записи в списочный справочник: - 3         
            - Поиск необходимого контакта по параметрам - 4                 
            - Удаление записи из строкового справочника по данным: - 5    
            - Удаление записи из списочного справочника по данным: - 6    
            - Очистка терминала - 7''')


def menu():
    flag = True
    while flag:
        book_all = {}
        init_dict(book_all, "str")
        init_dict(book_all, "lst")
        dict_command = {'1': print_book, '2': write_new_contact_str,
                        '3': write_new_contact_list, '4': search, '5': delete_contact_str, '6': delete_contact_list}
        print_hint()
        while True:
            command = input('Команда: > ')
            if command in dict_command:
                dict_command[command](book_all)
            else:
                print('Команда не распознана, попробуйте снова')
