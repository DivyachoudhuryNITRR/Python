#OOPS ::-->
#procedural oriented :->
# a=10
# b=20
# sum=a+b
# print(sum)
# diff=a-b
# print(diff)


#creating class
# class Student:
#     name="karan kumar"

#creating object (instances)
# s1=Student()
# s2=Student()
# print(s1.name)
# print(s2.name)


# class Car:
#     color="blue"
#     brand="merceedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)

# class Students:

#     name="anonymous"  #class attribute
#     college_name="ABC College"
#     #default constructors
#     # def __init__(self):
#     #     pass

#     #parameterised constructors
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):
#         print("Welcome Students,",self.name)
    
#     def get_marks(self):
#         return self.marks
        
# s1=Students("Karan",97)#object attributes
# # print(s1.name,s1.marks)
# # s2=Students("Arjun",98)
# # print(s2.name,s2.marks)
# # print(s2.college_name)
# s2=Students("Divya",99)

# s1.welcome()

# print(s1.get_marks())

# s2.welcome()
# print(s2.get_marks())



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod
#     def hello():
#         print("hello")
#     def avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("hi",self.name,"your avg score is : ",sum/3)
       

# s1=Student("Rakesh",[80,80,90])
# s1.avg() 

# s1.name="Divya"
# s1.avg()


# *************ABSTRACTIONS***********
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
    
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started...")
# car1=Car()
# car1.start()


class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance = ",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance = ",self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
