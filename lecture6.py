#Functions-->Block of statements that perform a specific task
 

# def calc_sum(a,b):
#     s=a+b
#     print(s)
# calc_sum(2,4)
# calc_sum(12,34)



#function definition
# def calc_prod(a,b): #parameters
#     return a*b
# prod=calc_prod(11,11)#function call; arguments
# print(prod)


# def printHello():
#     print("Hello World")
# for i in range(1,6):
#     printHello()

#average of 3 numbers:
# def avg(a,b,c):
#     average=(a+b+c)/3
#     return average
# avrg=avg(90,90,90)
# print(avrg)



#builtin Function:
# print("apnacollege","Shradhakhapra") #sep=" "
# print("apnacollege",end=" ") # to print on the same line
# print("Shradhakhapra")

# print()
# type()
# len()
# range()


#default parameters:
# non default arguments should be followed by default ones-->first non default then default

# def calc_prod(a,b=2):
#     print(a*b)
#     return a*b
# calc_prod(12)

# def length(list):
#     # print(len(list))
#     for i in range(1,len(list)+1):
#         print(i,end=" ")
# length([12,33,2,1,4])


# def fact(n):
#     p=1
#     for i in range(1,n+1,1):
#         p=p*i
#     print(p)   
# fact(6)

# 1USD==82.96INR
# def USDtoINR(n):
#     usd=82.96*n
#     print(usd)
# USDtoINR(2)

# def check(n):
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# check(241)

#Recursion:::

#recursive function
# def show(n):
#     if(n==10): #base case
#         return 
#     print(n)
#     show(n+1)
# show(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# f=fact(6)
# print(f)

# def add(n):
#     if(n==0):
#         return 0
#     else:
#         return n+add(n-1)
# a=add(10)
# print(a)

# def print_list(list,idx):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# print([1,2,3,4])