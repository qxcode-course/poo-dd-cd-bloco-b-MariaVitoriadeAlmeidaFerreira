class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, valor: str):
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]

        if valor not in tamanhosValidos:
            print("fail tamanho invalido")
            return
        
        self.__tamanho = valor

roupa = Roupa()

while True:
    line = input()
    args: list[str] = line.split(" ")
    print("$", line)

    if args[0] == "end":
        break
    elif args[0] == "show":
        print(f"size: ({roupa.getTamanho()})") 