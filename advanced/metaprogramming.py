class Meta(type):
    def __new__(cls, name, bases, dct):
        dct["custom_attr"] = "Hello"
        return super().__new__(cls, name, bases, dct)
class MyClass(metaclass=Meta):
    pass
print("Custom Attribute:", MyClass.custom_attr)