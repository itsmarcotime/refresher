# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'
    
    def has_birthday(self):
        self.age += 1


# extend class
class Customer(User):
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and i am {self.age} and my balance is {self.balance}'


# initialize user object
brad = User('Brad Chichi', 'chi@gmail.com', 25)

# initialize customer
perro = Customer('Judge', 'perro#yahoo.com', 23)

perro.set_balance(5000)

print(perro.greeting())

brad.has_birthday()
print(brad.greeting())