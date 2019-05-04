
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

	def get_book_on_loan(self):
		return self._books_on_loan

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




	def __str__(self):
		return f' ID:{self.get_id()},' \
			f' Name: {self.get_name()},' \
			f' Address: {self.get_address()}'
