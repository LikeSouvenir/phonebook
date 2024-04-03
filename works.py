import json
import easygui as eg

# проверяет данные, если файла нет, создает его со стандартными значениями
def load():
    try:
        with open ('telephonBook.json','r', encoding="utf-8") as phones:
            phonebook = json.load(phones)
    except:
        phonebook = {
    "Служба спасения": {'Телефон': [112], 
                        'День рождения': '01.01.1960', 
                        'email': "vanya@mail.ru" },
    "Служба доверия": { 'Телефон' : [88002000122, 5761010], 
                        'День рождения': '', 
                        'email': "" } 
    }
    return phonebook

# сохраняет измененные файлы перед выходом
def saveIfEnd():
    with open ('telephonBook.json','w', encoding="utf-8") as phones:
        phones.write(json.dumps(phonebook, ensure_ascii=False))

# вывод всех контактов
def all():
    allContact = ''
    for name, value in phonebook.items():
        allContact += "\n" + name
        for key, somePos in value.items():
            allContact += '\n' + key.ljust(15)+ str(somePos).replace('[', '').replace(']', ' ')
    eg.msgbox(msg = allContact, title='Контакты')
            
            
# поиск номеров по имени 
def find_number(name):
    try:
        pos = phonebook.get(name)
        ph = "".join(map(str, pos.get('Телефон')))
        bird = pos.get('День рождения')
        mail = pos.get('Email')
        print(f"Контакт - {name}\nТелефон - {ph}\nДень рождения - {bird}\nEmail - {mail}")
    except:
        print("Контакт не найден")

# добавление контакта
def add_phone_number(name, ph ,bird ,mail):
    phonebook[name] =  {
		'Телефон': [ph], 
        'День рождения': bird, 
        'Email': mail}
    return phonebook
    
# изменение контакта
def change_contact(name):
    if name not in phonebook:
        print("Такого контакта нет")
        return
    print('Что вы хотите поменять?\n (Вводите через пробел)\n')
    user_change = (input('1 - Телефон\n2 - День рождения\n3 - Email\n')).split()
    for i in set(user_change):
        if i == "1":
            ph = [(input(f"Введите новый номер телефонa, если несколько, то через ' , ': ")).split(',')]
        else:
            ph = phonebook.get(name).get("Телефон")
        if i == "2":
            dr = input(f"Введите новую дату дня рождения: ")
        else:
            dr = phonebook.get(name).get("День рождения")
        if i == "3":
            mail = input(f"Введите новую почту: ")
        else:
            mail = phonebook.get(name).get("Email")
        phonebook[name] =  {
                "Телефон" : ph,
                "Email" : mail,
                "День рождения" : dr}
    print("Изменения внесены")
    return phonebook
    
# удаление контакта
def delete_contact(name):
    phonebook.pop(name, "Такого контакта нет")
    print(f"Контакт {name} удален" if name not in phonebook else " ")
    return phonebook

# подгуржаются файлы с телефона
phonebook = load()
while True:
    user_choice = eg.integerbox(title = 'Что вы хотите сделать?', msg='\
        1 - Посмотреть контакты\n\
        2 - Найти контакт\n\
        3 - Добавить контакт\n\
        4 - Изменить контакт\n\
        5 - Удалить контакт\n\
        0 - Выйти из приложения',
        lowerbound = 0, upperbound = 5)
    if user_choice == 1:
        all()
    elif user_choice == 2:
        name = input("Введите искомое имя: ")
        find_number(name)
    elif user_choice == 3:
        name = input("Введите имя: ")
        ph = int(input("Введите телефон: "))
        bird = input("Введите день рождения: ")
        mail = input("Введите почту: ")
        add_phone_number(name, ph,bird,mail)
        pass
    elif user_choice == 4:
        name = input("Введите имя: ")
        change_contact(name)
        pass
    elif user_choice == 5:
        name = input("Введите имя: ")
        delete_contact(name)
        pass
    elif user_choice == 0:
        saveIfEnd()
        eg.msgbox(msg="До свидания!")
        break
    else:
        eg.msgbox(msg="Неправильно выбрана команда!")
        continue