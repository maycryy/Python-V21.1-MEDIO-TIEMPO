class Usuario:
    def __init__(self, name, email_address, balance) -> None:
            self.name = name
            self.email = email_address
            self.balance_mount = balance
    def hacer_deposito(self, amount):
        self.balance_mount += amount
    def hacer_retiro(self, other_user):
        self.balance_mount -= other_user
    def hacer_transferencia(self, other_user, amount):
        self.balance_mount += amount
        self.balance_mount -= amount
        self.imprime()
        self.imprime()

name ='pirata'
email='pirata@gmail.com'
balance = 1200
pirata= Usuario(name, email, balance)

name ='happy'
email='happy@gmail.com'
balance = 305
happy= Usuario(name, email, balance)

name ='rocky'
email='rocky@gmail.com'
balance = -7500
rocky= Usuario(name, email, balance)
print(f" user:{happy.name} , balance:{happy.balance_mount}")
print(f" user:{pirata.name} , balance:{pirata.balance_mount}")
print(f" user:{rocky.name} , balance:{rocky.balance_mount}")



happy.hacer_deposito(300)
happy.hacer_deposito(300)
happy.hacer_deposito(300)
happy.hacer_retiro(900)



print(f" user:{happy.name} , balance:{happy.balance_mount}")
print(f" user:{pirata.name} , balance:{pirata.balance_mount}")