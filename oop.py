opp= object orention programing language to map with real world scenarios, we started using object in code
# procedural type coding


# """a=10
# b=20

# sum=a+b
# print(sum)

# sub=a-b
# print(sub)

# a=40
# b=30

# sum=a+b
# print(sum)

# sub=a-b
# print(sub)"""

#function based programing- reusablity decrased + redundancy wil be reduced

"""def calc(a,b):
    sum=a+b
    print(sum)
    return sum  


calc(3,4)"""

#object oriented programing 

"""class Student:
    name="keshav"
    college
    
#create object(instances)   

s1=Student()
print(s1.name)

s2 = Student()
print(s2.name)
"""

"""class Car:
    color= "black"
    brand= "jaguar"
    interior="leather"

car1= Car()
print(car1.color,car1.brand,car1.interior)
 print(car1.brand)
 print(car1.interior)
print(car1)"""


#constructor 
"""all classes have a function called __init__() , which is always execute when the object is being intiated"""

"""class Student:
    def __init__(self):
        print("adding new student in database..")
        print(self)
s1=Student()"""


"""class Student:
    college_name = "rggec"
    def __init__(self,name,marks, age, roll_no,branch):
        self.name= name
        self.marks= marks
        self.age= age
        self.rollno= roll_no
        self.branch= branch
        print("adding new studnet in the database")

s1=Student("keshav",23.4,20,230,"ece")
print(s1.name,s1.marks,s1.age,s1.rollno,s1.branch)

s2=Student("khusbu",24.4,21,231,"ece")
print(s2.name,s2.marks,s2.age,s2.rollno,s2.branch)

print(s2.college_name,s1.college_name)"""

class Student:
    college_name= "rggec nagrota"


    def __init__(self,name,age):
        self.name= name
        self.age= age

    def welcome(self):
        print("welcome students",self.name)
        
    def your_age(self):
        print("your age",self.age)
    @staticmethod
    def hello():
        print("hello")

s1=Student("Khushbu+++",20)
s1.welcome()
s1.your_age()
s1.hello()