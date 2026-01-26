# List Methods
# Python has a set of built-in methods that you can use on lists.
# Method	Description
# append()	Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
# clear()	Removes all the elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# copy()	Returns a copy of the list
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
# count()	Returns the number of elements with the specified value
fruits = ["apple", "banana", "cherry", "banana", "cherry", "cherry"]
x = fruits.count("cherry")
print(x)
# Example 2
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# Example No.1
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
# Example No.2
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)
# index()	Returns the index of the first element with the specified value
# Example No.1
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
# Example No.2
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)
# Example No.3
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)
# insert()	Adds an element at the specified position
# Example No.1
fruits = ['apple', 'banana', 'cherry']
fruits.insert(0, "orange")
print(fruits)
# pop()	Removes the element at the specified position
# Example No.1
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
# Example No.2
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)
# remove()	Removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
# reverse()	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
# sort()	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)



