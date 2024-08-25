class Animal():
    type = 'dog'
    def __init__(self,name,age=0):
        self.name = name
        self.__age = age

    def eat(self):
        print(f'{self.type}is eating a bone')
