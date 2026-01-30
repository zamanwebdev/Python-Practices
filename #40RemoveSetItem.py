#40 Python Remove Set Item
MySet3 = {1,2,3,4,5,6,"Zaman", "Zahid", "Sumon"}
print(MySet3)
# MySet3.remove(10)
# MySet3.discard(10)
# MySet3.discard(4)
MySet3.discard("Sumon")
print(MySet3)
MySet3.pop()
print(MySet3)
MySet3.clear()
print(MySet3)