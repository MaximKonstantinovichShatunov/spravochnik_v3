def input_contact():
    return input('Введитe фамилию, имя, телефон, комментарий через пробел.\n').title().split()

def find_string(book):
    result = []
    ans = input(
        "Введите что либо, указывающее на конкретный контакт. Номер телефона, фамилию или имя:\n")
    for line in book:
        if ans.lower() in line.lower():
            result.append(line)
    return result

def print_contact(line):
    print(line)
    
def search(book):
    temp = book['str'] + book['lst']
    ser = find_string(temp)
    for i in set(ser):
        print_contact(i)

def find(book):
    ans = input("Введите что либо, указывающее на конкретный контакт. \n")
    for line in book:
        if ans.lower() in line.lower():
            return book.index(line)
    print('Такой записи нет!')


def delete_contact(book):
    index = find(book)
    print_contact(book[index])
    if input('Этот контакт будет удален!!! 1 - Да, 2 - Нет\n') == '1':
        print("Контакт удален!")
        return book[index]
    else:
        print("Контакт не удален!")

