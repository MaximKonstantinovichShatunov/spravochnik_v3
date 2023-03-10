import os
from readAndWrite import add_contact_str, add_contact_list, readfile_str, readfile_list
from printdist import print_list, print_str
from inputreplase import input_contact,delete_contact

file_book = {"str": 'Book1.txt', "lst": 'Book2.txt'}

def init_dict(book, key):
    if key == "lst":
        book[key] = readfile_list(file_book[key])
    else:
        book[key] = readfile_str(file_book[key])

def print_book(data):
    print_list(data['lst'])
    print()
    print_str(data["str"])


def write_new_contact_str(book):
    add_contact_str(file_book['str'], input_contact())
    init_dict(book, 'str')
    print()
    print("Контакт успешно добавлен!")

def write_new_contact_list(book):
    add_contact_list(file_book['lst'], input_contact())
    init_dict(book, 'lst')
    print()
    print("Контакт успешно добавлен!")


def delete_contact_str(book):
    repl = delete_contact(book['str'])
    if repl != '':
        with open(file_book["str"], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace((repl+'\n'), '')
        with open(file_book['str'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict(book, 'str')

def delete_contact_list(book):
    repl = delete_contact(book['lst'])
    if repl != '':
        with open(file_book['lst'], "r", encoding="utf_8") as s:
            allfile = s.read()
        allfile = allfile.replace('\n'.join(repl.split(', '))+'\n\n', '')
        with open(file_book['lst'], "w", encoding="utf_8") as s:
            s.write(allfile)
        init_dict(book, 'lst')
