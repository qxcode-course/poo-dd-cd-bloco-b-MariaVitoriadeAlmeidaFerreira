class Lead:
    def __init__(self, thickness:float, hardness:str, size:int ):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self):
        return self.__thickness
    
    def getHardness(self):
        return self