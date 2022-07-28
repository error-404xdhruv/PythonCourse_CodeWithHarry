class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayBooksList(self):
        for book in self.books:
            print(f"\t * ", {book})

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(
                f"Issue Successfully. Please return the book within 10 days and keep it safe.")
        else:
            print("Sorry, the book you want is currently unavailable.")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thank You.")


class student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input(
            "Enter the name of the book you want to return or append: ")
        return self.book


if __name__ == "__main__":
    while(True):
        welcomeMsg = '''
-------- Welcome to Library Management System --------
    \tPlease choose an option:
        1. List all the books.
        2. Request a Book
        3. Donate / Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        CentralLibrary = Library(["Data Structures and Algo", "Django", "CLRS", "Python Notes"])
        cmd = int(input("Enter your Choice: "))
        # since Python does not have switch case, we have   to use simple if else to go around
        if (cmd == 1):
            CentralLibrary.displayBooksList()
        elif (cmd == 2):
            CentralLibrary.borrowBooks(student.requestBook())
        elif (cmd == 3):
            CentralLibrary.returnBook(student.returnBook())
        elif (cmd == 4):
            print("Thanks for using our service.")
        else:
            print("Invalid Choice.")