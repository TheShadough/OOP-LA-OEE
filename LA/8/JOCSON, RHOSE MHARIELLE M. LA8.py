class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
book = Book("Safe Skies Archer", "Gwy Saludes")
print(f"Book: {book.title},  {book.author}")
del book.author
print(book.author)

bukk = Book("My Husband is a Mafia Boss", "Yanalovesyouu")
print(f"Book: {bukk.title},{bukk.author}")