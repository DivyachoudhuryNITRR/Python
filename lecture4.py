# info={
#     "key":"value",
#     "name":"apnacollege",
#     "learning":"coding",
#     "age":37,
#     "is_adult":True,
#     "topics":("dict","set"),
#     "subjects":["python","C","Java"]
# }
# print(info)
# print(type(info))
# print(info["name"])
# print(type(info["topics"]))
# info["name"]="Divya" #overwrite
# info["surname"]="Choudhury"
# print(info)


# null_dict={}
# null_dict["name"]="apnacollege"
# print(null_dict)

# NESTED DICTIONARIES
# student={
#     "name":"Rahul",
#     "subjects":{
#         "chem":97,
#         "math":99,
#         "social":100
#     }
# }
# print(student)
# print(len(tuple(student.keys())))
# print(tuple(student.values()))

# print(list(student.items()))


# print(student["name1"]) #ERROR
# print(student.get("name1")) # None

# student.update({"city":"delhi"})
# print(student)

#SET
# collections={1,2,2,2,3,"hello","hi",4} #unordered
# print(collections)
# print(type(collections))
# print(len(collections))#duplicate items are not counted

# collection=set()#empty set; syntax
# # print(type(collection))
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(3)
# # collection.remove(8)# error


# collection.add("apnacollege")
# collection.add((1,3,2,9))
# # collection.add([1,3,2,9])
# # collection.clear()
# collection.pop()
# collection.pop()
# print(collection)

# set1={1,2,3,2,3,5,6}
# set2={1,4,3,2}
# set=set1.union(set2)
# name=set1.intersection(set2)
# print(set)
# print(name)

# word={
#     "table":("a piece of furniture","list of facts & figures"),
#     "cat":"a small animal"
# }
# print(word)


# set={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(set))
 

# marks={}
# x=int(input("enter phy : "))
# marks.update({"phy":x})
# x=int(input("enter chem : "))
# marks.update({"chem":x})
# x=int(input("enter maths : "))
# marks.update({"maths":x})
# print(marks)

# values={9,"9.0"}
# print(values)

# values={("int",9),("float",9.0)}
# print(values)