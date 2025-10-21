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
        self.__assento: Person | None = None
        self.__power: int = power
        self.__time: int = 0

    def inserirPessoa(self, person: Person) -> bool:
        if self.__assento == None:
            self.__assento = person
            return True
        else:
            print("fail: busy motorcycle")
            return False
        
    def remover(self) -> Person | None:
        if self.__assento != None:
            aux = self.__assento 
            self.__assento = None
            return aux
        else:
            print("fail: empty motorcycle")
            return None

        