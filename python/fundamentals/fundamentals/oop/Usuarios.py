class Usuario:
    def __init__(self, name, email_address, balance) -> None:
            self.name = name
            self.email = email_address
            self.balance_mount = balance
    def hacer_deposito(self, amount):
        self.balance_mount += amount
        return self
    def hacer_retiro(self, other_user):
        self.balance_mount -= other_user
        return self
    def imprime (self):
        print(f"{self.name}  monto {self.balance_mount}")
        return self
    def hacer_transferencia(self, amount, user):
        self.balance_mount += amount
        user.balance_mount -= amount
        self.imprime()
        user.imprime()
        return self

name ='pirata'
email='pirata@gmail.com'
balance = 0
pirata= Usuario(name, email, balance)
    
name ='happy'
email='happy@gmail.com'
balance = 0
happy= Usuario(name, email, balance)

name ='rocky'
email='rocky@gmail.com'
balance = 0
rocky= Usuario(name, email, balance)

print(f" user:{happy.name} , balance:{happy.balance_mount}")
print(f" user:{pirata.name} , balance:{pirata.balance_mount}")
print(f" user:{rocky.name} , balance:{rocky.balance_mount}")

happy.hacer_deposito(300).hacer_deposito(300).hacer_deposito(300).balance_mount
rocky.hacer_transferencia(1000,happy)


print(f" user:{happy.name} , balance:{happy.balance_mount}")
print(f" user:{pirata.name} , balance:{pirata.balance_mount}")