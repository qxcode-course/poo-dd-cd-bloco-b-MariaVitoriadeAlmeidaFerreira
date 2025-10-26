class Pessoa:
    def __init__(self, nome:str, dinheiro:int):
        self.__nome: str = nome
        self.__dinheiro: int = dinheiro

    def getNome(self) -> str:
        return self.__nome
    
    def getDinheiro(self) -> int:
        return self.__dinheiro
    
    def __str__(self) -> str:
        return f"{self.__nome}:{self.__dinheiro}"
    
class Moto:
    def __init__(self):
        self.__custo: int = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def Driver(self, motorista: Pessoa) -> None:
        if self.__motorista == None:
            self.__motorista = motorista
        
    def

    
    def __str__(self) -> str:
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"

def main():
    moto = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str]  = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            motorista = Pessoa(args[1], int(args[2]))
            moto.Driver(motorista)

main()

    