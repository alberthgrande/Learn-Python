class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages."

    def __eq__(self, other):
        return self.pages == other.pages 

book_1 = Book('The Great Gatsby', 180)
book_2 = Book('To Kill a Mockingbird', 180)

print(len(book_1))
print(len(book_2))
print(str(book_1))
print(str(book_2))
print(len(book_1) == len(book_2))