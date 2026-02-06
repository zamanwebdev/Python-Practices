#75 Python Introducing All About Method
class ClassName():
    def InstanceMethod(self):
        print("Hello Instance Method")
    @classmethod
    def ClassMethod(self):
        print("This is Class Method")
    @staticmethod
    def StaticMethod():
        print("This is Static Method")

obj = ClassName()
obj.InstanceMethod()

ClassName.ClassMethod()
obj.StaticMethod()