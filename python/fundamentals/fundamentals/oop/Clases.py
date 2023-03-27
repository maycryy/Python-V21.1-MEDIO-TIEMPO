class Usuario:		
    name_bank="banco estado"
    def __init__(self, name, email_address) -> None:
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount        
name ='ba'
email='ba@gmail.com'
guido= Usuario(name, email)
name='k'
email='k@gmail.com'
monty= Usuario(name, email)

guido.hacer_depósito(100)
print(f" 1 {guido.balance_cuenta}")

guido.hacer_depósito(500)
print(f" 2 {guido.balance_cuenta}")

guido.hacer_depósito(950)
print(f" 3 {guido.balance_cuenta}")

# Accediendo a los atributos de la instancia
print(f" 1 {guido.name}")	# salida: Michael
print(f" 2 {guido.email}")
print(f" 3 {monty.name}")	# salida: Michael
print(f" 4 {monty.email}")



'''
guido.name = "Guido"
guido.email ="Guido@gmail.com"
monty.name = "Monty"
monty.email = "Monty@gmail.com"

print(f"1 {guido.name}")
print(f"2 {guido.email}")
print(f"3 {monty.name}")
print(f"4 {monty.email}")
'''


