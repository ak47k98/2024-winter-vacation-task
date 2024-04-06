class Person :
    def __int__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")





person_1 = Person("Alice", 30)



# 调用对象的方法
person_1.say_hello()