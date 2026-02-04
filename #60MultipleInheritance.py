#60 Python Multiple Inheritance
class baba:
    Car = "BMW"
    Tk = "100 Koti"
    Home = "10 Flat"

class baba2:
    SmartPhone = "Iphone"
    AC = "Walton"
    Microphone= "fifine"
class baba3:
    Webcam = "fifine k6"
    Laptop = "Laptop"
    Camera = "Camera"

class Kaka(baba, baba2, baba3):
    BrokenPhone ="Nokia"
    BrokenHome = "Matir Bari"

k = Kaka()
print(k.Car)
print(k.SmartPhone)
print(k.Webcam)