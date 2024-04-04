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
    
def change_contact():
    name = eg.textbox(title= "Изменение контакта", msg="Введите имя: ")
    if name not in phonebook:
        eg.msgbox(msg = f'Контакт {name} не найден', title='Изменение контакта')
        return
    ph = mail = dr = None
    while(True):
        user_change = eg.buttonbox(msg = str(phonebook.get(name)).replace('[', '').replace(']', ' ').replace("'", ""),
            title="Изменение контакта",
            choices=('Телефон', 'День рождения','Email', 'Закончить'))
        if user_change == "Телефон":
            ph = eg.textbox(title= "Изменение контакта", msg="Введите телефон (если несколько, то через пробел): ")
            ph = ph.split()
        if user_change == "День рождения":
            dr = eg.textbox(title= "Изменение контакта", msg="Введите день рождения: ")
        if user_change == "Email":
            dr = eg.textbox(title= "Изменение контакта", msg="Введите Email: ")
        if user_change == "Закончить":
            break
    if ph == None:
        ph = phonebook.get(name).get("Телефон")
    if dr == None:
        dr = phonebook.get(name).get("День рождения")
    if mail == None:
        mail = phonebook.get(name).get("Email") 
    phonebook[name] =  {
                "Телефон" : ph,
                "Email" : mail,
                "День рождения" : dr}
    eg.msgbox(msg = name + "\n" + str(phonebook.get(name)).replace('[', '').replace(']', '').replace("'", "") + "\nКонтакт изменен.",
              title='Изменение контакта')
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