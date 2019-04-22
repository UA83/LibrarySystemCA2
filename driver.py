from items import list_of_book, list_of_periodical
from Book import Book
from helper import *
BOOK_NOT_FOUND = 'Item Not Found'
BOOK_ADDED = 'Book Added Successfully'

#display all books
def display_all_books():
    get_page_title('Display Items')
    for b in list_of_book:
        print(b)

display_all_books()







#Search Book
def search_item():
    get_page_title('Search Item')
    to_search = input('### TIP --> You can search by ID, Title, Publish Year, ISBN or Author ###'
                      '\nPlease Enter the item to be search:')

    x = Book.find_item(list_of_book, str(to_search))
    if not x:
        print(BOOK_NOT_FOUND)
    else:
        for b in x:
            print(b)

search_item()






# add book
def add_book():
    get_page_title('Add Book')

    # get the latest ID
    last_id = get_latest_id()
    isbn = input('Enter ISBN:')
    title = input('Enter Title:')
    author = input('Enter Author:')
    year = input('Enter Year:')

    # Use the latest ID and add 1 to it, e.g 10 + 1 = 11 < new ID to be used.
    new_book = Book(str(int(last_id)+1),isbn, title, author, year)

    list_of_book.append(new_book)
    print(new_book)
    print(BOOK_ADDED)

add_book()



