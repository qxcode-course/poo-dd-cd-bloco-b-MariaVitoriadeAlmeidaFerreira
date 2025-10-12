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
            print("fail")