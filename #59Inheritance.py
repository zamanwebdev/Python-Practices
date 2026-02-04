#59 Python Inheritance
class baba:
    Car = "BMW"
    Tk = "100 Koti"
    Home = "10 Flat"
class Kaka(baba):
    BrokenPhone ="Nokia"
    BrokenHome = "Matir Bari"

k = Kaka()
print(k.Home)
print(k.BrokenPhone)
