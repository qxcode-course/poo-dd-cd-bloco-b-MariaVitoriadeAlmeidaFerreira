class Lead:
    def __init__(self, thickness:float, hardness:str, size:int ):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self):
        return self.__thickness
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size:int):
        self.__size = size
    
    #sena pelo o amor de Deus que nome é esse
    def usagepersheet(self) -> int:
        if self.__thickness == 'HB':
            return 1
        elif self.__thickness == '2B':
            return 2
        elif self.__thickness == "4B":
            return 4
        elif self.__thickness == "6B":
            return 6
        return 0
    
    def __str__(self):
        return f"{self.__thickness}:{self.__hardness}: {self.__size}"
    
class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip: Lead | None

    def HasGrafite(self) -> bool:
        if self.__tip != None:
            return True

    def insert(self, lead: Lead) -> bool:
        if self.HasGrafite():
            print("")
            return False
        self.__tip = lead
        return True