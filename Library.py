class library:
  def __init__(self,no_books,books):
    self.books = books
    self.no_books = no_books

  def show(self):
    print(f"This Library have {self.no_books} number of books and these are {self.books}")

  def enterbook(self,book):
    self.books.append(book)
    self.no_books += 1

  
  def check(self):
    l = len(self.books)
    if l != self.no_books:
      print("Your program have mistake the len of books and numbers of books isn't matching")
    else:
      print("Everything is okay")


# listofbooks = ['1984','The Lord','Kite','Harry Potter','Five','Lion','Mockingbird','Thief']
# lib1 = library(8,listofbooks)
# lib1.show()
# lib1.enterbook('magistic')
# lib1.show()
# lib1.check()

listbook = ['Rings','Wardrobe','Harper','Markus','Zusak']
lib2 = library(5,listbook)
lib2.show()
lib2.enterbook('roses')
lib2.show()
lib2.check()
