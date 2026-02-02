thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("All key names is bellow : ")
for x in thisdict:
    print(x)
print("All values Name is bellow : ")
for x in thisdict:
    print(thisdict[x])
print("use the values() method to return values of a dictionary: ")
for x in thisdict.values(): print(x)
print("use the keys() method : ")
for x in thisdict.keys(): print(x)
print("use the items() method : ")
for x,y in thisdict.items(): print(x,y)
