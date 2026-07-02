numbers = {1,2,3,4,4,5,5,6,7}
print(numbers)

# operations/methods
# add()
number = set()
print(number)
number.add(1)
number.add(2)
number.add(20.5)
number.add("aibo8")
print(number)

#remove()
number.remove(20.5)
print(number)


#pop()
print(number.pop())
print(number)

#clear
print(number.clear())
print(number)

set1 = {1,2,3,3,5,5,5,6}
set2 = {4,5,6,7,8,9}
print(set1.union(set2))
print(set1.intersection(set2))