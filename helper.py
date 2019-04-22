from items import *

def numDigits(n):
    n_str = str(n)
    return len(n_str)

# Print the title of the pager where the user is navigating.
def get_page_title(page_title):
    print(page_title + '\n' + len(page_title) * '=')

# Get the latest ID use
def get_latest_id():
    l = []
    for b in list_of_book:
        l.append(b.get_item_id())

    for p in list_of_periodical:
        l.append(p.get_item_id())

    # sort list, as the values are string, I am using (key=int) to sort it as integers.
    l.sort(key=int)

    # Return the last value of the list.
    return l[-1]

# Check if the ISBN is in use
def get_isbn():
    for b, in list_of_book:
        l = []
        l.append(b.get_isbn())

    return l

def check_isbn(list_isbn, check_isbn):
    if check_isbn in list_isbn:
        return False
    return True