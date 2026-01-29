#To add one item to a set use the add() method.
MySet1 = {"apple", "banana", "cherry"}
MySet1.add("orange")
print(MySet1)
# To add items from another set into the current set, use the update() method.
MySet2 = {1,2,3,4}
MySet1.update(MySet2)
print(MySet1)
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)