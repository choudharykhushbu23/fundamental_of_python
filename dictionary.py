dict={
    "name":"khushbu",
    "age":"20.10",
    "roll no":36,
    "college":"RGGEC"
}
print(dict)

# for finding a value in dictionary
print(dict["name"])

#  for change the value in dictionary
dict["name"] = "Anchal","Khushbu","Riya"
print(dict)

#add new key
dict["city"]="kangra"
print(dict)


# Null dictionary
null_dict = {}
print(null_dict)

# add elements/values in null dictionary
null_dict["name"] = "khushbu"
null_dict["age"] = 20.10
null_dict["roll no"] = 36
print(null_dict)

# nested dictionary
student = {
    "name":"khushbu",
    "sub":{
        "VLSI":90,
        "Mobile comm.":95,
        "CN":99
    },
    "sem":6
}
print(student["sub"]["CN"])
student["sub"]["math"]=80
print(student)

# Dictionary method for acces a element/values
#.keys
#.values()
#.item()
#.get()
# update(new dict)

print(student.keys())

# to convert in list
print(list(student.keys()))

# list operations
print(len(student.keys()))

print(student.values())
print(len(student.values()))

print(student.items())

# Two methods to access the keys of dictionary
#1
print(student["name"])
print(student.get("name"))

student.update({"surname":"choudhary"})
print(student)