
def main_menu():
	commands = ['Показать все контакты',
				'Открыть файл',
				'Сохранить файл',
				'Новый контакт',
				'Изменить контакт',
				'Удалить контакт',
				'Найти контакт',
				'Выйти из прграммы']
	print('\nВыберите пункт меню:')
	
	for i in range(len(commands)):
		print(f'\t{i + 1}. {commands[i]}')
	user_input = 0
	while (user_input < 1 or user_input > 8):
		user_input = int(input('\nВведите пункт меню:'))
	
	print()
	return user_input


def show_contacts(phone_book: list):
	if len(phone_book) > 0:
		for i, item in enumerate(phone_book):
			print(f'{i+1} {item[0]} {item[1]} ({item[2]})')
	else:
		print('Телефонная книга пустая или не загружена')
	

def load_success():
	print('Телефонная книга загружена успешно')
  

def save_success():
	print('Телефонная книга успешно сохранена')


def new_contact():
	new = []
	name = input('Введите Имя и Фамилию контакта: ')
	phone = input('Введите номер телефона: ')
	comment = input('Введите комментарий к контакту: ')
	return name, phone, comment

def find_contact():
	search = input('Введите искомое значение: ')
	return search
	
def choose_contact(phone_book: list, flag: int):
	if flag:
		str = '\nВведите номер контакта который хотите удалить: '
	else:
		str = '\nВведите номер контакта который хотите отредактировать: '
	while True:
		num = int(input(str))
		if num < 1 or num > len(phone_book) :
			print('Контакта с таким номером не существует')
		else:
			return num
			
def delite_success(delite_num: int):
	print(f'Контакт {delite_num} успешно удален')


def edit_contact(contact: list):
	print(f'\nРедактируемый контакт:\n\t{contact[0]} {contact[1]} ({contact[2]})')
	print('Введите новые данные, если данные не изменились, нажмите \"Enter\"')
	edited = list(new_contact())
	if (len(edited[0]) == 0):
		edited[0] = contact[0]
	if (len(edited[1]) == 0):
		edited[1] = contact[1]
	if (len(edited[2]) == 0):
		edited[2] = contact[2]
	return edited
	
def ask_about_saving():
	while 1:
		choise = input('Хотите сохранить изменения в справочнике? Нажмите N/Y: ')
		if choise == 'n' or choise == 'N':
			return False
		elif choise == 'y' or choise == 'Y':
			return True
		else:
			print('Некорректный ввод')
