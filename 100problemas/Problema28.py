class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        """Inicializa la cuenta con un saldo inicial."""
        self.saldo = saldo_inicial
    
    def deposito(self, cantidad):
        """Realiza un depósito en la cuenta."""
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Has depositado {cantidad}.")
        else:
            print("La cantidad de depósito debe ser positiva.")
    
    def retiro(self, cantidad):
        """Realiza un retiro de la cuenta."""
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Has retirado {cantidad}.")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad de retiro debe ser positiva.")
    
    def consultar_saldo(self):
        """Consulta el saldo actual de la cuenta."""
        print(f"Tu saldo actual es: {self.saldo}")


cuenta = CuentaBancaria(1000)
cuenta.consultar_saldo()
cuenta.deposito(500)
cuenta.consultar_saldo()
cuenta.retiro(300)
cuenta.consultar_saldo()
cuenta.retiro(2000) 
cuenta.consultar_saldo()
