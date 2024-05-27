'''
6. Create the custom Python classes which have methods and attributes and implement single inheritance,
 multiple inheritance, and multilevel inheritance
'''

class Books:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def details(self):
        return (f"Name: {self.name}\nAuthor: {self.author}")

'''Fiction inherits Books- 
Single inheritance'''
class Fiction(Books):
    def __init__(self, name, author, genre):
        super().__init__(name, author)
        self.genre = genre

    def details(self):
        return f"{super().details()}\nGenre: {self.genre}"
'''
Multiple inhericance
'''
class Paperback:
    def __init__(self, pages):
        self.pages = pages

    def get_length(self):
        return f"Pages: {self.pages}"

'''FictionPaperback inheritis from both Fiction and Paperback'''

class FictionPaperback(Fiction, Paperback):
    def __init__(self, name, author, genre, pages):
        Fiction.__init__(self, name, author, genre)
        Paperback.__init__(self, pages)

    def details(self):
        return f"{super().details()}\n{self.get_length()}"


'''Multi level inheritance'''
class NonFiction(Books):
    def __init__(self, name, author, subject):
        super().__init__(name, author)
        self.subject = subject

    def details(self):
        return f"{super().details()}\nSubject: {self.subject}"


class NonFictionPaperback(NonFiction, Paperback):
    def __init__(self, name, author, subject, pages):
        NonFiction.__init__(self, name, author, subject)
        Paperback.__init__(self, pages)

    def details(self):
        return f"{super().details()}\n{self.get_length()}"

fiction_book = Fiction("ABc", "xyz", "Fantasy")
print(fiction_book.details())
