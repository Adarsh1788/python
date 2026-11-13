#create a class publisher (name).derive class book from publisher with attributes title and author
#derive class python from book with attributes price and no of pages write a program that displays information about the python book
#use base classes constructor invocation and method over riding
class publisher: 
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Publisher Name:", self.name)
class Book(publisher):
    def __init__(self, name, title, author):
        publisher.__init__(self, name)
        self.title = title
        self.author = author
    def display(self):
        publisher.display(self)
        print("title: ",self.title)
        print("author : ",self.author)
class python(Book):
    def __init__(self, name, title, author,price,pages):   
     Book.__init__(self,name,title,author)
     self.price=price
     self.pages =pages 
    def display(self):
        publisher.display(self)
        Book.display(self)
        print("pages :",self.pages)
        print("price :",self.price)
n=input("enter the name of the publisher")
t=input("enter the title of the book")
a=input("enter the name of the author")
p=int(input("enter the price"))
pa=int(input("enter the no of pages"))

p=python(n,t,a,p,pa)
p.display()
        