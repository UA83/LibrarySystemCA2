
class User():

	def __init__(self, id, name, address):

		self._id = id
		self._name = name
		self._address = address
		self._books_on_loan = None

	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def get_address(self):
		return self._address

	# Should I have this option here? I dont think so. but just for the sake I will leave it here
	def set_id(self, id):
		self._id = id

	def set_name(self, name):
		self._name = name

	def set_address(self, address):
		self._address = address

	def borrow_book(self, book):
		self._books_on_loan = book
		book._onloan = True

	def find_user(list_users, to_search):
		list_of_users_found = []
		for u in list_users:
			if to_search.lower() in str(u.get_name()).lower():
				list_of_users_found.append(str(u))
		return list_of_users_found



	def __str__(self):
		return f' ID:{self.get_id()},' \
			f' Name: {self.get_name()},' \
			f' Address: {self.get_address()}'
