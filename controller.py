import model
import view

def start():
	user_choice = 0
	while user_choice != 8:
		user_choice = view.main_menu()
		
		match user_choice:
			case 1:
				phone_book = model.get_phone_book()
				view.show_contacts(phone_book)
			case 2:
				model.open_phone_book()
				view.load_success()
			case 3:
				model.save_phone_book()
				view.save_success()
			case 4:
				new = list(view.new_contact())
				model.update_phone_book(new)
			case 5:
				phone_book = model.get_phone_book()
				view.show_contacts(phone_book)
				editable_num = view.choose_contact(phone_book, False)
				contact = model.get_contact(editable_num)
				edited_contact = view.edit_contact(contact)
				phone_book = model.change_contract(editable_num, edited_contact)
				view.show_contacts(phone_book)
			case 6:
				phone_book = model.get_phone_book()
				view.show_contacts(phone_book)
				delite_num = view.choose_contact(phone_book, True)
				phone_book = model.delite_contact(delite_num)
				view.show_contacts(phone_book)
				view.delite_success(delite_num)
				pass
			case 7:
				search = view.find_contact()
				result = model.search_contact(search)
				view.show_contacts(result)
	if(model.check_need_save()):
		if(view.ask_about_saving()):
				model.save_phone_book()			
