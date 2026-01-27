'''
import sys
# print(sys.version)
'''
# Exercises No.1
'''
x,y,z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)
'''
# Exercises No.2
'''
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])
'''
# Exercises No.3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
# Exercises No.4

# Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)
# Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)
# Select the correct function to remove all items from a list:

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
# What is a correct syntax for looping through the items of a list?

for x in ['apple', 'banana', 'cherry']:
  print(x)
# Insert the missing part of the while loop below to loop through the items of a list.
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1
# What is a correct syntax for looping through the items of a list?

[print(x) for x in ['apple', 'banana', 'cherry']]
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
print(newlist)


#28Exercise-02


