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
def find_number():
    name = eg.textbox(title= "Поиск контакта", msg="Введите искомое имя: ")
    pos = phonebook.get(name)
    eg.msgbox(msg = str(pos).replace('[', '').replace(']', '').replace("'", ""),title='Поиск контакта')

# добавление контакта
def add_phone_number():
    name = eg.textbox(title= "Добавление контакта", msg="Введите имя: ")
    ph = eg.textbox(title= "Добавление контакта", msg="Введите телефона (если несколько, то через пробел): ")
    bird = eg.textbox(title= "Добавление контакта", msg="Введите день рождения: ")
    mail = eg.textbox(title= "Добавление контакта", msg="Введите Email: ")
    ph = ph.split()
    phonebook[name] =  {
		'Телефон': [ph], 
        'День рождения': bird, 
        'Email': mail}
    pos = phonebook.get(name)
    eg.msgbox(msg = name + "\n" + str(pos).replace('[', '').replace(']', '').replace("'", "") + "\nКонтакт добавлен.",
              title='Добавление контакта')
    
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
        find_number()
    elif user_choice == 3:
        add_phone_number()
        pass
    elif user_choice == 4:
        change_contact()
        pass
    elif user_choice == 5:
        delete_contact()
        pass
    elif user_choice == 0:
        saveIfEnd()
        eg.msgbox(msg="До свидания!")
        break
    else:
        eg.msgbox(msg="Неправильно выбрана команда!")
        continue