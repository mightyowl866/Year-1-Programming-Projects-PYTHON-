class Library:
    def __init__(self,name):
        self.__name = name
        self.__books_for_authors = {}

    def add_author(self,author):
        if author not in self.__books_for_authors:
            self.__books_for_authors[author] = []
    
    def add_book(self,book,author):
        self.add_author(author)
        self.__books_for_authors[author].append(book)
    def __str__(self):
        result = ""
        result += self.__name + '\n'
        for (author, book_list) in self.__books_for_authors.items():
            result += author + str(book_list) + '\n'
        return result
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self,new_name):
        self.__name = new_name

class BookLibrary(Library):
    def foo(self):
        print(self.name)
cna_lib = Library('CNA Library')

cna_lib.add_book('The Firm','John Grisham')
cna_lib.add_book('The Runaway Jury','John Grisham')
cna_lib.add_book('Bitch bitch','fuckboy chris')
print(cna_lib)

cna_lib.add_book("Da Vinci Code", "Dan Brown")

cna_lib.add_author("Steven King")