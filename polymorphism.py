#POLYMORPHISM :--> Operator Overloading
#when the same operator is allowed to have different meaning according to the context.
#many forms
#operators & Dunder functions
# a+b #addition a.__add__(b)
# a-b #subtraction a.__sub__(b)
# a*b #multiplication a.__mul____(b)
# a/b #division a.__truediv_____(b)
# a%b #addition a.__mod____(b)


# Decorator
# @getter
# @setter


# meaning of + is different in every context
# print(1+2) #3
# print("apna"+"college") #concatenate-->apnacollege
# print([1,2,3]+[4,5,6]) #concatenate-->[1,2,3,4,5,6]

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def showNumber(self):
#         print(self.real,"i + ",self.img,"j")
    
#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
#     def __sub__(self,num2):
#         newReal=self.real-num2.real
# #         newImg=self.img-num2.img
# #         return Complex(newReal,newImg)
# # num1=Complex(1,3)
# # num1.showNumber()
# # num2=Complex(2,4)
# # num2.showNumber()

# # # num3=num1.add(num2)
# # # num3.showNumber()
# # num3=num1+num2
# # num3.showNumber()

# # num3=num1-num2
# # num3.showNumber()

# class Circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*self.r**2
#     def perimeter(self):
#         return 2*3.14*self.r
# c1=Circle(2)
# print(c1.area())
# print(c1.perimeter())


# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showDetails(self):
#         print("role = ",self.role)
#         print("Department = ",self.department)
#         print("salary = ",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT","75,000")
# # e1=Employee("accountant","Finance","60,000")
# # e1.showDetails()

# engg1=Engineer("Elon Mosk","48")
# engg1.showDetails()


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price>odr2.price
odr1=Order("chips",20)
odr2=Order("tea",15)
print(odr1>odr2) #true


