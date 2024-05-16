# ここにコードを書いてください
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title, author):
        self.books.append({"title":title, "author":author})
    def remove_book(self, title):
        self.books = [book for book in self.books if book["title"]!=title]
    def retrieve_books(self):
        return self.books