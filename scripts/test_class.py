class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        return (f'{self.name} is {self.age} years old')

Alice = Person('alice',7)
print(Alice.hello())
