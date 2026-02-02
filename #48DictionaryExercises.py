# Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)
thisdict = dict.fromkeys(x)
print(thisdict)
# Get the value of the "model" item:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "bro")
print(x)
y = car.setdefault("color", "White")
print(y)