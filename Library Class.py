class Library:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print("issued")
        else:
            print("not available")

    def return_book(self):
        self.available = True
        print("returned")

    def status(self):
        print(self.name, self.available)

b = Library("book1", "author1")
b.checkout()
b.status()
b.return_book()