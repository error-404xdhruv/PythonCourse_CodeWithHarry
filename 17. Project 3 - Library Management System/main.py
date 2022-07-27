class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayBooksList (self):
        for book in self.books:
            print(f"\t * ", {book})
    def borrowBooks (self, bookName):
        if bookName in self.books:
            print(f"Issue Successfully. Please return the book within 10 days and keep it safe.")
        else:
            print("Sorry, the book you want is currently unavailable.")
    def returnBook (self, bookName):
        self.books.append(bookName)
        print("Thank You.")


class student:
    