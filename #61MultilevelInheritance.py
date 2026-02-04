class Baba:
    Car = "BMW"
    Tk = "100 Koti"
    Home = "10 Flat"

class Son1(Baba):
    SmartPhone = "Iphone"
    AC = "Walton"
    Microphone= "fifine"
class Son2(Son1):
    Webcam = "fifine k6"
    Laptop = "Laptop"
    Camera = "Camera"

class Son3(Son2):
    BrokenPhone ="Nokia"
    BrokenHome = "Matir Bari"

S3 = Son3()
print(S3.Home)
print(S3.SmartPhone)
print(S3.Webcam)
print(S3.BrokenPhone)