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
    
    def receber(self, dinheiro:int) -> None:
        self.__dinheiro += dinheiro

    def pagar(self, dinheiro:int) -> None:
        self.__dinheiro -= dinheiro
    
    def setDinheiro(self, dinheiro:int) -> None:
        self.__dinheiro = dinheiro
    
class Moto:
    def __init__(self):
        self.__custo: int = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def Driver(self, motorista: Pessoa) -> None:
        if self.__motorista == None:
            self.__motorista = motorista
        
    def Pass(self, passageiro: Pessoa) -> None:
        if self.__passageiro == None:
            self.__passageiro = passageiro

    def Drive(self, km: int) -> None:
        self.__custo += km
    
    def Left(self) -> Pessoa | None:
        if self.__passageiro != None:
            aux = self.__passageiro
            self.__passageiro.pagar(self.__custo)
            if self.__passageiro.getDinheiro() < 0:
                self.__passageiro.setDinheiro(0)
                print("fail: Passenger does not have enough money")
            self.__motorista.receber(self.__custo)
            self.__custo = 0
            self.__passageiro = None
            return aux
        
        
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
        elif args[0] == "setPass":
            passageiro = Pessoa(args[1], int(args[2]))
            moto.Pass(passageiro)
        elif args[0] == "drive":
            km = int(args[1])
            moto.Drive(km)
        elif args[0] == "leavePass":
            pessoa = moto.Left()  
            print(f"{pessoa} left")




main()

    