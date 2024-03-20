#File I/O :-->

#Open,Read,&close file ::
# f=open("demo.txt","r")
# # data=f.read(6)#to read all the characters
# # data=f.read(6)#NUMBER of characters to read
# # line1=f.readline()
# # print(line1)

# line2=f.readline()
# print(line2)
# # print(data)
# # print(type(data))

# line3=f.readline()
# print(line3)
# f.close()
# C:\Users\divya\OneDrive\Desktop\PROJECTS FOR PLACEMENT'\py_python\Python\demo.txt-->path location


#WRITING TO A FILE
# # f=open("demo.txt",'w') #-->overwrite
# f=open("demo.txt",'a') #add the new  data
# # f.write("I want to learn Javascript tomorrow. 123")
# f.write("\nAfter trhat nodejs")
# f.close()

# f=open("sample.txt","w") #creates a new file if the named file does not exist
# f.close()

# f=open("sample.txt",'a') # creates a new file if not exists
# f.close()

#combination of mode__.-->

# f=open("demo.txt","a+") #r+,w+
# f.write("abc")
# print(f.read())
# f.close()


# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

# import os
# os.remove("sample.txt")


# f=open("practice.txt","r")
# # f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
# data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)
# f.close()
# f=open("practice.txt","w") 
# f.write(new_data)

# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word)!=-1):
#             print("Found")
#         else:
#             print("Not Found")

# # check_for_word()

# def check_for_line():
#     word="let"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1
# print(check_for_line())


count=0
with open("practice.txt","r") as f:
    data=f.read()
    print(data)


    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
           
            count+=1
    print(count)

    # num=""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(num)
    #         num=""
    #     else:
    #         num+=data[i]




    



