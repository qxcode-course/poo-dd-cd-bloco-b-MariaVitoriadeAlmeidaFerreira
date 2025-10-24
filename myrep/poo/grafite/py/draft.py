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

    def usageper
    
    def __str__(self):
        return f"{self.__thickness}:{self.__hardness}: {self.__size}"