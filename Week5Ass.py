# Assignment 1:  Designing my class! 
# parent class
class Book:
    def __init__(self, title, author, price, genre):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre

    def get_info(self):
        return f"{self.title} by {self.author} - ${self.price}"

# Child class
class EBook(Book):
    def __init__(self, title, author, price, genre, file_size):
        super().__init__(title, author, price, genre)
        self.file_size = file_size

    # Polymorphism: same method name, different behavior
    def get_info(self):
        return f"{self.title} (EBook) by {self.author} - ${self.price} - {self.file_size}MB"


book1 = Book("Let Them", "Mel Robbins", 20, "Motivational")
ebook1 = EBook("All Men in Lagos are Mad", "Damilare Kuku", 10, "Fiction", 5)

print(book1.get_info())
print(ebook1.get_info())


# Assignment 2: Polymorphism Challenge!

class animal:
    def action (self):
        return "Animal is making a sound"

class dog(animal):
    def action (self):
        return "Dog is barking"

class cat(animal):
    def action (self):
        return "Cat is meowing"

class cow(animal):
    def action (self):
        return "Cow is mooing"
    
class sheep(animal):
    def action (self):
        return "Sheep is bleating"
    
for animal in (dog(), cat(), cow(), sheep()):
    print(animal.action())