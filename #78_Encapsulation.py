#78 Python Encapsulation
class Parent:
    def __init__(self,Name,FatherName):
        self.__Name = Name
        self.__FatherName = FatherName
        print(self.__Name)
        print(self.__FatherName)
p1 = Parent("Zaman","Rahman")
# print(p1.Name)
# print(p1.FatherName)


