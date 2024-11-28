class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"\"{self.title}\" by {self.author}"

book1 = Book("The Shining", "Stephen King")
book2 = Book("1984", "George Orwell")

print(book1)
print(book2)
