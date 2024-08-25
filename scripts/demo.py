# 面向对象 a.创建一个Animal类，name属性设置为实例属性且可传递参数，然后age属性设置为私有初始值为0，
# type属性设置为类属性值为狗; 设置一个实例方法eat()，打印狗吃骨头(放入一个模块中-模块名tools)
# b.重新创建一个demo.py文件，引入tools模块，然后定义一个Dog类，继承Animal，重写里面的eat()，
# 在原有基础上（狗吃骨头）, 添加打印内容;吃完骨头摇摇头...

from tools import Animal
class Dog(Animal):
    def __init__(self,name,age=0):
        super().__init__(name,age)
    def eat(self):
        super().eat()
        print('shake the head after eating')
if __name__ == '__main__':
    my_dog = Dog('Huckie',7)
    my_dog.eat()

