# Python Remove List Item
# Remove Specified Item
thislist=["apple","banana","cherry", 420]
print(thislist)
thislist.remove("banana")
thislist.remove(420)
print(thislist)
# The pop() method removes the specified index.
thislist.pop()
thislist.pop()
print(thislist)
# The del keyword also removes the specified index:
NewList = ["Zaman", "Sumon", "Zahid"]
print(NewList)
del NewList[1]
print(NewList)
# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)