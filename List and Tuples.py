# student1 = "khusbu"
# student2 = "muskan"
# student3 = "anchal"
# student4 = "riya"
# student5 = "sourav"
# student6 = "aditya"
# student7 = "rudraksh"
# student8 = "vaishali"
# student9 = "keshav"

# studentsName = ["khusbu","muskan","anchal","riya","sourav","aditya","rudraksh","vaishali","keshav"]

# print(studentsName)
# print(studentsName[0])
# print(studentsName[2])
# print(studentsName[6])
# print(studentsName[7])
# print(studentsName[1],studentsName[3],studentsName[4])
# print(studentsName[5],studentsName[8])


# studentsName.append("shanu")
# print(studentsName)
# studentsName.remove("muskan")
# print(studentsName)

# Numbers = [1,2,3,4,5,6,7,8,9,10]
# Numbers.reverse()
# print(Numbers)
# Numbers.sort()
# print(Numbers)
# Numbers.remove(6)
# print(Numbers)

# Num = [1,2,3,3,4,5,6,8]
# a = Num.count(3)
# print(a)


# Assignment 1
# create a tuple
Numbers = (10,20,30,40,50,60,70,80,90,100)
print(Numbers)

# Change tupple into a list
my_list = list(Numbers)
print(my_list)

# List operations
# append()
my_list = [10,20,30,40,50,60,70,80,90,100]
my_list.append(110)
print(my_list)

# insert()
my_list.insert(1,15)
print(my_list)

# extend()
my_list.extend([110,120,130,140])
print(my_list)

# remove()
my_list.remove(50)
print(my_list)

# pop()
my_list.pop(5)
print(my_list)

# clear()
my_list.clear()
print(my_list)

# len()
my_list1 = [1,2,3,4,5,6,7,8,9,10]
print(len(my_list1))

# sort()
my_list1.sort()
print(my_list1)

# reverse()
my_list1.reverse()
print(my_list1)

# count()
print(my_list1.count(6))

# copy()
new_list = my_list1.copy()
print(new_list)

# Convert again into tuple
tuple1 = tuple(new_list)
pri++nt(tuple1)