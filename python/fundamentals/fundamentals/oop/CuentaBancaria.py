class CuentaBancaria:
    def __init__(self, cuentas, tasa_interés, balance): 
        self.cuentas = cuentas
        self.balance_mount = balance
        self.intereses = tasa_interés
        self.tasa_interés= tasa_interés

    def deposito(self, amount):
        self.balance_mount += amount 
        return self
    
    def retiro(self, other_user):
        self.balance_mount -= other_user
        return self

    def mostrar_info(self):
        print(f"{self.cuentas} Balance: {self.balance_mount}")
        return self
    
    def generar_interés(self):
        print(f"{self.cuentas} Balance: {self.balance_mount}")
        self.balance_mount += self.balance_mount * self.intereses
        return self
    
cuentas="childish"
balance = 0
tasa_interés = 0.5
childish = CuentaBancaria(cuentas,tasa_interés ,balance)

cuentas="dirtybwoi"
balance=1000
tasa_interés=0.7
dirtybwoi= CuentaBancaria(cuentas, tasa_interés,balance)

dirtybwoi.retiro(100).deposito(200.5).generar_interés().retiro(1500).mostrar_info()
childish.deposito(300).deposito(14.5).generar_interés().mostrar_info()

