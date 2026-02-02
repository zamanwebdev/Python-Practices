#46 Python Dictionaries
# The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.pop("model")
# print(thisdict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# thisdict.popitem()
# print(thisdict)
# del thisdict["model"]
# del thisdict
thisdict.clear()
print(thisdict)