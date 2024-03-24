#del keyword
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Divya")
# # print(s1.name)
# del s1.name
# print(s1.name)


#public & private:
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
# acc1=Account("12345","abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Person:
#     __name="anonymous"
#     @staticmethod
#     def __hello():
#         print("hello person")

#     def welcome(self):
#         self.__hello()

# p1=Person()
# print(p1.welcome())


# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("Car started...")
    
#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)#inheritating parent class
#         # self.name=name
#         super().start()
#         super().stop()

# car1=ToyotaCar("prius","electric")
# print(car1.type)





# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type

# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")
# car1=Fortuner("diesel")
# print(car1.start())
# print(car1.stop())


# class A:
#     varA="welcome to class A"
# class B:
#     varB="welcome to class B"
# class C(A,B):
#     varC="welcome to class C"
# c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#problem with staticmethod --> they can't access or modify class state & generally for utility.
#classMethod :-
# a class method is bound to the class & receives the class as an implicit first argument.


# class Person:
#     name="anonymous"

#     @classmethod #classmethod decorator
#     def changeName(cls,name):
#         cls.name=name

#     # def changeName(self,name):
#     #     # self.name=name
#     #     # Person.name=name #in order to change the name in class
#     #     self.__class__.name=name #in order to change the name in class
# p1=Person()
# p1.changeName("Divya Choudhury")
# print(p1.name)#this did not change the class attribute rather created a new instance of name.and
#  #there are 2 different attribute for name one in class and other in the className
# print(Person.name)


# 3 types of function :-
#  1.static method #that do not change and has access both the class and instance methods
#  2.class method (cls) #class as argument
#  3.instance method(self) #instance attributes 

#PROPERTY DECORATOR :-->
# we use @property decorator on any method in the class to use the method as a property.
# attribute value-->depends on functions ==we can make function as attribute
class Student:
    
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    # def calcPercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"


stu1=Student(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage)