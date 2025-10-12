class Watch:
    def __init__(self, hour:int = 0, minute:int = 0, segundo:int = 0):
        self.__hour = 0
        self.__minute = 0
        self.__segundo = 0
        
        self.setHour(hour)
        self.setMinute(minute)
        self.setSegundo(segundo)

    def getMinute(self) -> int:
        return self.__minute
    
    def getHour(self) -> int:
        return self.__hour
    
    def getSegundo(self) -> int:
        return self.__segundo
    
    def setHour(self, valor:int):
        if valor < 0 or valor > 23:
            print("fail: hora invalida")
            return
        self.__hour = valor 

    def setMinute(self, valor: int):
        if valor < 0 or valor > 59:
            print("fail: minuto invalido")
            return
        self.__minute = valor
    
    def setSegundo(self, valor: int):
        if valor < 0 or valor > 59:
            print("fail: segundo invalido")
            return 
        self.__segundo = valor

    def __str__(self) -> str:
        hour = self.getHour()
        minute = self.getMinute()
        segundo = self.getSegundo()
        return f"{hour:02}:{minute:02}:{segundo:02}"
    
    def nextSegundo(self) -> None:
        self.__segundo += 1
        if self.__segundo >= 60:
            self.__segundo = 0
            self.__minute += 1
        if self.__minute >= 60:
            self.__minute = 0
            self.__hour += 1
        if self.__hour >= 24:
            self.__hour = 0


def main():
    relogio = Watch(0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(relogio)
        elif args[0] == "end":
            break
        elif args[0] == "init":
            relogio = Watch(int(args[1]), int(args[2]), int(args[3])) 
        elif args[0] == "set":
            relogio.setHour(int(args[1]))
            relogio.setMinute(int(args[2]))
            relogio.setSegundo(int(args[3]))
        elif args[0] == "next":
            relogio.nextSegundo()
        else:
            print("fail")


main()