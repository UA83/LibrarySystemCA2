from helper import *

BOOK_ADDED = ' Book Added Successfully'
BOOK_NOT_FOUND = ' Book Not Found'
USER_ADDED = ' User Added Successfully'
USER_DELETED = ' User Deleted Successfully'
USER_NOT_FOUND = ' User Not Found'


def display_menu():
    print(' Library System')
    print(' ---------------------------------')
    print(' ----- Users                     |')
    print(' | 1.  Add User #                  |')
    print(' | 2.  Delete User               |')
    print(' | 3.  Display Users #             |')
    print(' | 4.  Search User #              |')
    print(' ----- Books                     |')
    print(' | 5.  Add Book #                 |')
    print(' | 6.  Borrow Book               |')
    print(' | 7.  Delete Book               |')
    print(' | 8.  Display Books #            |')
    print(' | 9.  Return Book               |')
    print(' | 10. Search Book #              |')
    print(' ----- Periodicals               |')
    print(' | 11. Add Periodical            |')
    print(' | 12. Delete Periodical         |')
    print(' | 13. Display Periodicals       |')
    print(' | 14. Search Periodical         |')
    print(' -------                         |')
    print(' | X.  Exit                      |')
    print(' ---------------------------------\n')


# [1] Add User
def add_user():
    get_page_title('Add User')

    # get the latest ID
    last_id = get_latest_id('for_user')
    print(last_id)

    # Add a check name? nahhhhh =============================================
    name = input(' Enter Name:')
    address = input(' Enter Address:')
    # Use the latest ID and add 1 to it, e.g 10 + 1 = 11 < new ID to be used.
    new_user = User(str(int(last_id) + 1), name, address)

    list_users.append(new_user)
    print(new_user)
    print(USER_ADDED)


# [2] Delete USer
def delete_user():
    get_page_title('Delete User')
    id = input(' === TIP --> if you do not know the user ID, press x to exit and chose option 4 from the menu to search the User ID. ===\n'
               ' Enter User ID to be deleted:')

    while not id.isdigit():
        if id.lower() == 'x':
            break
        id = input(
            ' === TIP --> if you do not know the user ID, press x to exit and chose option 4 from the menu to search the User ID. ===\n'
            ' Enter User ID to be deleted:')

    for u in list_users:
        if u.get_id() == id:
            get_index = list_users.index(u)
            delete = input(f' ** Delete User{u}** ? | [Yes/No]')
            # Add while loop here
            if delete.lower() == 'yes':
                print(f' User {u} Deleted Successfully')
                del list_users[get_index]
            else:
                print(f' User {u} | User not Deleted')
        else:
            print('User not found')


# [3] Display Users
def display_users():
    get_page_title('Display Users')
    for u in list_users:
        print(u)


# [4] Search User
def search_user():
    get_page_title('Search User')

    to_search = input(' === TIP --> You can search User by ID, Name or Address. ==='
                      '\n Please Enter a user data to be search:')
    found = User.find_user(list_users, str(to_search))
    if not found:
        print(USER_NOT_FOUND)
    else:
        for u in found:
            print(u)
    total = len(found)

    place_holder = 'Users were'
    if total < 2:
        place_holder = 'User was'
    print(f' The total of: {total} {place_holder} found')


# [5] Add Book
def add_book():
    get_page_title('Add Book')

    # get the latest ID
    last_id = get_latest_id()

    isbn = input(' Enter ISBN:')
    # get a list with all ISBNs in the library
    l_isbn = get_isbns()

    # Check if it is used
    is_isbn_used = check_isbn(l_isbn, isbn)
    print(is_isbn_used)

    # check if isbn is number, the length and if it is already used
    while not isbn.isdigit() or len(isbn) != 13 or is_isbn_used:
        isbn = input(' Try again, Enter ISBN:')
        l_isbn = get_isbns()
        is_isbn_used = check_isbn(l_isbn, isbn)
        print(is_isbn_used)

    # title can contain different characters
    title = input(' Enter Title:')

    # Maybe add a validation here, name is name
    author = input(' Enter Author:')

    # check if year is number and if it has 4 digits
    year = input(' Enter Year:')
    while not year.isdigit() or len(year) != 4:
        year = input(' Try Again, Enter Year:')

    # Use the latest ID and add 1 to it, e.g 10 + 1 = 11 < new ID to be used.
    new_book = Book(str(int(last_id) + 1), title, year, isbn, author)

    list_of_book.append(new_book)
    print(new_book)
    print(BOOK_ADDED)


# [6] Borrow Book
def borrow_book():
    get_page_title('Borrow Book')


# [7] Delete Book
def delete_book():
    get_page_title('Delete Book')


# [8] Display Books
def display_books():
    get_page_title('Display Books')
    for b in list_of_book:
        print(b)


# [9] Return Book
def return_book():
    get_page_title('Return Book')


# [10] Search Book
def search_book():
    get_page_title('Search Book')
    to_search = input(' === TIP --> You can search by ID, Title, Publish Year, ISBN or Author ==='
                      '\n Please Enter the item to be search:')

    found = Book.find_item(list_of_book, str(to_search))
    if not found:
        print(BOOK_NOT_FOUND)
    else:
        for b in found:
            print(b)

    total = len(found)

    place_holder = 'Books were'
    if total < 2:
        place_holder = 'Books was'
    print(f'The total of: {total} {place_holder} found')


# [11] Add Periodical
def add_periodical():
    get_page_title('Add Periodical')


# [12] Delete Periodical
def delete_periodical():
    get_page_title('Delete Periodical')


# [13] Display Periodicals
def display_periodicals():
    get_page_title('Display Periodicals')


# [14] Search Periodical
def search_periodical():
    get_page_title('Search Periodical')


display_menu()

# Ask the user to choose a number on the menu
opt = input(' Please enter a option:')

# Program terminates when user enters [x] or [X]
while opt.upper() != 'X':

    # [1] Add User
    if opt == '1':
        add_user()

    # [2] Delete USer
    elif opt == '2':
        delete_user()

    # [3] Display Users
    elif opt == '3':
        display_users()

    # [4] Search User
    elif opt == '4':
        search_user()

    # [5] Add Book
    elif opt == '5':
        add_book()

    # [6] Borrow Book
    elif opt == '6':
        borrow_book()

    # [7] Delete Book
    elif opt == '7':
        delete_book()

    # [8] Display Books
    elif opt == '8':
        display_books()

    # [9] Return Book
    elif opt == '9':
        return_book()

    # [10] Search Book
    elif opt == '10':
        search_book()

    # [11] Add Periodical
    elif opt == '11':
        add_periodical()

    # [12] Delete Periodical
    elif opt == '12':
        delete_periodical()

    # [13] Display Periodicals
    elif opt == '13':
        display_periodicals()

    # [14] Search Periodical
    elif opt == '14':
        search_periodical()

    # Invalid Option
    else:
        print(' === Option Invalid, Please try again ===\n')

    display_menu()
    opt = input(' Please enter a valid option:')

prog_end = ' === The system has terminated ===\n'
print(f'{prog_end.upper()}')
# ===================================================================================
