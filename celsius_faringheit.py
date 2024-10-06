class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def to_fahrenheit(self, celsius):
        self.__celsius = celsius
        return celsius * 9 / 5 + 32

    def get_celsius(self):
        return self.__celsius


temp = Temperature(77)
print(temp.to_fahrenheit(77))
print(temp.get_celsius())