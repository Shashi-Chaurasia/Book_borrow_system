class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvilableBooks(self):
        print("Books present in this labrary are : ")
        for book in self.books:
            print("\t*"+book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(
                f"You have been essue {bookName} book please keep it safe and return on time within 15 days")
            self.books.remove(bookName)
            return True
        else:
            print(
                f"Sorry this {bookName} book is already issue by some one else or either not avilable ! plz wait until he reyturn ")
            return False
            
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning book , Hope you enjoy reading !")


class Student:
    def requestBook(self):
        self.books = input(
            "Enter the book name which you want to borrow :books:")
        return self.books

    def returnBook(self):
        self.books = input(
            "Enter the book name which you want to return :books:")
        return self.books


if __name__ == "__main__":
    MitaoeLibrary = Library(["ULYSSES by James Joyce", "THE GREAT GATSBY", "A PORTRAIT OF THE ARTIST AS A YOUNG MAN", "LOLITA", "BRAVE NEW WORLD",
                             "THE SOUND AND THE FURY", "DARKNESS AT NOON", "SONS AND LOVERS", "INVISIBLE MAN",
                             "python", "Django", "James Smith", "Data Structure", "Algorithms", "Java", "php", "Android", "Ctr"])
    MitaoeLibrary.displayAvilableBooks()
    students = Student()

    while(True): 
        librariMsg = ''' ===========Welcome to Mitaoe Library =================
        please choose a option : 

        1 - listing All book
        2 - request a book
        3 - Add / returnBook 
        4 - exit from library

        '''

        print(librariMsg)

        user = input("Enter your chooise : ")
        if user == '1':
            MitaoeLibrary.displayAvilableBooks()

        elif user == '2':
            MitaoeLibrary.borrowBooks(students.requestBook())

        elif user == '3':
            MitaoeLibrary.returnBook(students.returnBook())

        elif user == '4':
            exit()

        else:
            print("Wrong chooise ! plz choose correct chooise")
