import collections 

phone_book = []
path = 'phone_book.txt'

def get_phone_book():
	global phone_book
	return phone_book

def update_phone_book(contact: list):
	global phone_book
	phone_book.append(contact)

def load_data():
	global path
	data = []
	local_phone_book = []
	with open(path, 'r', encoding='UTF-8') as file:
		data = file.readlines()
	for line in data:
		local_phone_book.append(line.strip().split(';'))
	return local_phone_book

def open_phone_book():
	global phone_book
	phone_book = load_data()
	  
def save_phone_book():
	global phone_book
	global path
	data = []
	for line in phone_book:
		data.append(';'.join(line))
	with open(path, 'w', encoding='UTF-8') as file:
		data = file.write('\n'.join(data))	  
	  
def search_contact(search: str):
	global phone_book
	search_results = []
	for line in phone_book:
		for field in line:
			if search in field:
				search_results.append(line)
				break
	return search_results
	
def delite_contact(del_num: int):
	global phone_book
	phone_book.pop(del_num-1)
	return phone_book
	
def get_contact(num: int):
	global phone_book
	return phone_book[num-1]
	
def change_contract(num: int, contact: list):
	global phone_book
	phone_book[num - 1] = contact
	return phone_book
	
def check_need_save():
	global phone_book
	local_phone_book = load_data()
	if len(phone_book) != len(local_phone_book):
		return True
		
	for i in range(len(phone_book)):
		if collections.Counter(phone_book[i]) != collections.Counter(local_phone_book[i]):
			return True
	return False
		
	
