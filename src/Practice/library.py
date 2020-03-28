'''
class => Library
layers of abstraction => display available books, to lend a book, to add a book

class => customer
layers of abstraction => request for a book, return a book
'''

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books")
        for book in self.availableBooks:
            print(book)

    def lendbook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")


    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank you!")

class Customer:
    def requestBook(self):
        print("Enter a name of a book you would like to borrow: ")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning")
        self.book = input()
        return self.book

library = Library(['Think and Grow Rich','Who will cry when you die', 'For one more day'])

customer = Customer()
while True:

    print("Enter 1 to display the available book")
    print("Enter 2 top request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice=int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    if userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendbook(requestedBook)
    if userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    if userChoice is 4:
        quit()

