class Person:
    def __init__(self, name: str, age:int):
        self.__name: str = name
        self.__age: int = age


    def getAge(self) -> int:
        return self.__age

    def getName(self) -> str:
        return self.__name
    
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"
    
class motinha:
    def __init__(self, power:int = 1):
        self.__person: Person | None 
        self.__power: int = power
        self.__time: int = 0


        