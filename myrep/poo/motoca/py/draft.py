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

    def comprarTempo(self, time: int) -> None:
        self.__time += time

    def dirigir(self, time:int) -> None:
        if self.__time == 0:
            print("fail: buy time first")
            return
        
        if self.__assento == None:
            print("fail: empty motorcycle")
            return
        
        if self.__assento.getAge() > 10:
            print("fail: too old to drive")
            return
        
        if self.__time <= time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= time

    def honk(self) -> None:
        honk: str = "P"
        for i in range(self.__power):
            honk += "e"
        honk += "m"
        print(honk)
    
    def getPerson(self) -> Person | None:
        return self.__assento
    
    def getPower(self) -> int:
        return self.__power
    
    def getTime(self) -> int:
        return self.__time
    
    def __str__(self) -> str:
        aux = ""
        if self.__assento != None:
            aux = f"{self.__assento}"
        else:
            aux = "empty"
            
        return f"power:{self.__power}, time:{self.__time}, person:({aux})"
    
def main():
    moto = motinha | None = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            people = Person(nome, idade)
            moto.inserirPessoa(people)
        elif args[0] == "init":
            power = int(args[1])
            moto = motinha(power)
        elif args[0] == "leave":  
            aux = moto.remover()
            if aux != None:
                print(aux)
        elif args[0] == "buy":
            time = int(args[1])
            moto.comprarTempo(time)
        elif args[0] == "drive":
            time = int(args[1])
            moto.dirigir(time)
        elif args[0] == "honk":
            moto.honk()
            
main()