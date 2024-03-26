# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author #instant attribute
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
    # TODO: create instance methods #function has-attr checks if an attribute exists 
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price 
    
    def setdiscount(self, amount):
        self._discount = amount #underscore in front of the discount to give a hint that this attribute is considered internal to the class and is not for public consumption.

# TODO: create some book instances
b1 = Book("War and Peace","Leo Tolstoy", 1555,39.90)
b2 = Book("The Catcher in the Rye","JD Salinger",243,29.85)

# # TODO: print the price of book1
# print(b1.getprice())

# # TODO: try setting the discount
# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)
#subclasses 