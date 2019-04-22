# Populates the library system with books.
# id(h) | isbn | title(h) | author | year(h) | on_loan
# id(h) | title(h) | year(h) | isbn | author
from Book import Book
from Periodical import Periodical

#List of books
list_of_book = [Book('1', 'A Game of Thrones', '1996', '9780553573404', 'George R. R. Martin'),
                Book('12', 'A Clash of Kings', '1998', '9753407447831', 'George R. R. Martin'),
                Book('3', 'A Storm of Swords', '2000', '9789573029348', 'George R. R. Martin'),
                Book('4', 'A Feast for Crows', '2005', '9786857302245', 'George R. R. Martin'),
                Book('6', 'Test for ID', '2019', '7823612876545', 'Ulisses Alves'),
                Book('5', 'A Dance with Dragons', '2011', '9798310843234', 'George R. R. Martin')]

#Periodicals have a ID, title, year, an editor, volume, issue.
#Periodicals can’t be loaned.
list_of_periodical = [Periodical('35', 'How does it work?', '1983', 'Ulisses Mirage', '3', '123'),
                      Periodical('88', 'Adventures of a dog called Suki', '2019', 'Stephanie Enders', '7', '456')]

