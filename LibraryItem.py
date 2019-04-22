
class LibraryItem:
	def __init__(self, item_id, title, year):
		self._item_id = item_id
		self._title = title
		self._year = year

	def get_item_id(self):
		return self._item_id

	def set_item_id(self, item_id):
		self._item_id = item_id

	def get_title(self):
		return self._title

	def set_title(self, title):
		self._title = title

	def get_year(self):
		return self._year

	def set_year(self, year):
		self._year = year

	def find_item(list_of_book, to_search):
		list_of_books_found = []
		for b in list_of_book:
			if to_search.lower() in str(b).lower():
				list_of_books_found.append(str(b))
		return list_of_books_found

	def __str__(self):
		return f'ID:{self.get_item_id()}, Title:{self.get_title()}, Years:{self.get_year()}'
