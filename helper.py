from items import *

def numDigits(n):
    n_str = str(n)
    return len(n_str)


# Print the title of the pager where the user is navigating.
def get_page_title(page_title):
    print(' ' + page_title + '\n ' + len(page_title) * '=')


# Get the latest ID used
def get_latest_id(choice=None):
    list_of_ids = []
    if choice == 'for_user':
        for u in list_users:
            list_of_ids.append(u.get_id())

    else:
        # Getting all books ID
        for b in list_of_book:
            list_of_ids.append(b.get_item_id())

        # Getting all Periodicals ID
        for p in list_of_periodical:
            list_of_ids.append(p.get_item_id())

    # sort list, as the values are string, I am using (key=int) to sort it as integers.
    list_of_ids.sort(key=int)

    # Return the last value of the list, which is the highest number.
    return list_of_ids[-1]


# Return a list with all ISBN in the Library
def get_isbns():
    list_isbn = []
    for b in list_of_book:
        list_isbn.append(b.get_isbn())

    return list_isbn


# Check if ISBN is already in use, returns True/False
def check_isbn(list_isbn,  check_isbn):
    if check_isbn in list_isbn:
        return True
    return False
