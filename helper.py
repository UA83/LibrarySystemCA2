from items import *

def numDigits(n):
    n_str = str(n)
    return len(n_str)


# Print the title of the pager where the user is navigating.
def get_page_title(page_title):
    print(' ' + page_title + '\n ' + len(page_title) * '=')


# Get the latest ID use
def get_latest_id(choice=None):
    l = []
    if choice == 'for_user':
        for u in list_users:
            l.append(u.get_id())

    else:
        for b in list_of_book:
            l.append(b.get_item_id())

        for p in list_of_periodical:
            l.append(p.get_item_id())

    # sort list, as the values are string, I am using (key=int) to sort it as integers.
    l.sort(key=int)

    # Return the last value of the list.
    return l[-1]


# Return a list with all ISBN in the Library
def get_isbns():
    l = []
    for b in list_of_book:
        l.append(b.get_isbn())

    return l


# Check if ISBN is already in use, returns True/False
def check_isbn(list_isbn,  check_isbn):
    if check_isbn in list_isbn:
        return True
    return False
